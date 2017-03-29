from __future__ import unicode_literals

import os
import json
import base64
from datetime import datetime
import hashlib
import hmac
from time import mktime
from wsgiref.handlers import format_date_time

# from .packages.requests.auth import AuthBase
from six.moves.urllib.parse import urlparse

CONTENT_TYPE = 'application/vnd.api+json'

class ApiAuthentication(object):
    def __init__(self, method, url, body):
        self.access_key_id = os.environ.get('ESP_ACCESS_KEY_ID', None)
        self.secret_access_key = os.environ.get('ESP_SECRET_ACCESS_KEY', None)
        self.method = method
        self.url = url
        self.body = body
        self.date = None  # set at the time of __call__ in case of reuse

    def auth_headers(self):
        """
        :return: dict of headers necessary for ESP API HMAC authentication
        :rtype: dict
        """
        self.date = self._request_date()
        headers = {}
        headers['Authorization'] = self.sign_request()
        headers['Content-MD5'] = self.body_md5()
        headers['Content-Type'] = CONTENT_TYPE
        headers['Accept'] = CONTENT_TYPE
        headers['Date'] = self.date
        return headers

    def _request_date(self):
        now = datetime.now()
        tt = mktime(now.timetuple())
        return format_date_time(tt)

    def body_md5(self):
        """
        :return: A base64 string of the content body passed in.
        :rtype: str
        """
        if not self.body:
            body = ''
        else:
            body = json.dumps(self.body)
        body_bytes = body.encode('utf-8')
        b64 = base64.b64encode(hashlib.md5(body_bytes).digest())
        return b64.decode()

    def sign_request(self):
        """
        :return: Sign request takes pieces of information about the request and
        generates a hmac hash digest for authentication. This will return a
        base64 string of the digest
        :rtype: str
        """
        url = urlparse(self.url)
        uri = url.path
        if url.query != '':
            uri += '?{}'.format(url.query)
        canonical = '{method},{content_type},{md5},{uri},{date}'.format(
            method=self.method.upper(),
            content_type=CONTENT_TYPE,
            md5=self.body_md5(),
            uri=uri,
            date=self.date)
        digest = hmac.new(self.secret_access_key.encode('utf-8'),
                          canonical.encode('utf-8'),
                          digestmod=hashlib.sha1).digest()
        return 'APIAuth {access_key}:{signature}'.format(
            access_key=self.access_key_id,
            signature=base64.b64encode(digest).decode())

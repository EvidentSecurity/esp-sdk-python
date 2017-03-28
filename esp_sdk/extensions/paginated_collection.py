from __future__ import absolute_import

from ..models.paginated_collection import PaginatedCollection
from six.moves.urllib.parse import parse_qs, urlparse


class PaginatedCollection(PaginatedCollection):
    # @PaginatedCollection.links.setter
    # def links(self, links):
    #     PaginatedCollection.links = links
    #     self.__parse_pagination_links()

    def __init__(self, data=None, included=None, links=None):
        # create a local cache for memoization
        self._local_cache = {}
        super(PaginatedCollection, self).__init__(data, included, links)

    def __iter__(self):
        # return iter(self.data)
        for i in self.data:
            yield i
        if self.has_next_page:
            for n in self.next_page():
                yield n

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def first_page(self):
        if self.has_previous_page:
            return self._updated_collection({'number': 1})
        else:
            return self

    def previous_page(self):
        if self.has_previous_page:
            return self._updated_collection(self.previous_page_params)
        else:
            return self

    def next_page(self):
        if self.has_next_page:
            return self._updated_collection(self.next_page_params)
        else:
            return self

    def last_page(self):
        if not self.is_last_page:
            return self._updated_collection(self.last_page_params)
        else:
            return self

    def page(self, page_number=None):
        if page_number is None:
            raise ValueError('You must supply a page number.')
        if int(page_number) < 1:
            raise ValueError('Page number cannot be less than 1.')
        if int(page_number) > int(self.last_page_number):
            raise ValueError('Page number cannot be greater than the last page number.')


        if int(page_number) != int(self.current_page_number):
            return self._updated_collection({'number': str(page_number), 'size': (self.next_page_params or self.previous_page_params)['size']})
        else:
            return self

    @property
    def current_page_number(self):
        previous = self.previous_page_number
        page = '1'
        if previous:
            page = str(int(previous) + 1)
        return page

    @property
    def previous_page_number(self):
        return self.previous_page_params.get('number', None)

    @property
    def next_page_number(self):
        return self.next_page_params.get('number', None)

    @property
    def last_page_number(self):
        return self.last_page_params.get('number', None)

    @property
    def has_previous_page(self):
        return self.previous_page_number is not None

    @property
    def has_next_page(self):
        return self.next_page_number is not None

    @property
    def is_last_page(self):
        return self.last_page_number is None

    @property
    def next_page_params(self):
        if 'next_page_params' not in self._local_cache:
            self._local_cache['next_page_params'] = {}
            if 'next' in self.links:
                # parse the query string for the ids
                url = urlparse(self.links['next'])
                if url.query:
                    next_url = parse_qs(url.query)
                    self._local_cache['next_page_params'] = {'number': str(int(float(next_url['page[number]'][0]))), 'size': str(int(float(next_url['page[size]'][0])))}
        return self._local_cache['next_page_params']

    @property
    def previous_page_params(self):
        if 'previous_page_params' not in self._local_cache:
            self._local_cache['previous_page_params'] = {}
            if 'prev' in self.links:
                # parse the query string for the ids
                url = urlparse(self.links['prev'])
                if url.query:
                    previous_url = parse_qs(url.query)
                    previous_dict = {'number': str(int(float(previous_url['page[number]'][0])))}
                    # The last page may not contain the full per page number of records, and will therefore come back with an incorrect size since the
                    # size is based on the collection size.  This will mess up further calls to previous_page or first page so remove the size so it will bring back the default size.
                    if not self.is_last_page and 'page[size]' in previous_url:
                        previous_dict['size'] = str(int(float(previous_url['page[size]'][0])))
                    self._local_cache['previous_page_params'] = previous_dict
        return self._local_cache['previous_page_params']

    @property
    def last_page_params(self):
        if 'last_page_params' not in self._local_cache:
            self._local_cache['last_page_params'] = {}
            if 'last' in self.links:
                # parse the query string for the ids
                url = urlparse(self.links['last'])
                if url.query:
                    last_url = parse_qs(url.query)
                    self._local_cache['last_page_params'] = {'number': str(int(float(last_url['page[number]'][0]))), 'size': str(int(float(last_url['page[size]'][0])))}
        return self._local_cache['last_page_params']

    def _updated_collection(self, params):
        post_params = [('page', params)]
        post_params = post_params + [p for p in self._post_params if p[0] != 'page']
        return self._api_client.call_api(self._resource_path, self._method,
                                        self._path_params,
                                        self._query_params,
                                        self._header_params,
                                        body=self._body,
                                        post_params=post_params,
                                        files=self._files,
                                        response_type=self._response_type,
                                        auth_settings=self._auth_settings,
                                        callback=self._callback,
                                        _return_http_data_only=self._return_http_data_only,
                                        _preload_content=self._preload_content,
                                        _request_timeout=self._request_timeout,
                                        collection_formats=self._collection_formats)

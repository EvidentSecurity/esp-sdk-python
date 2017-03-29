from __future__ import absolute_import

from ..models.paginated_collection import PaginatedCollection
from six.moves.urllib.parse import parse_qs, urlparse


class PaginatedCollection(PaginatedCollection):
    """
    A PaginatedCollection object is returned on any api object that returns a
    paginated list from the ESP API.  Mostly the api list endpoints.

    This is an override of the auto generated PaginatedCollection class to
    provide the functions necessary for pagination.
    """

    def __init__(self, data=None, included=None, links=None):
        """
        Overidden initializer to add additional attributes
        """
        # create a local cache for memoization
        self._local_cache = {}
        super(PaginatedCollection, self).__init__(data, included, links)

    def __iter__(self):
        """
        Iterator to loop over the entire paginated collection in data.

        """
        for i in self.data:
            yield i
        if self.has_next_page:
            for n in self.next_page():
                yield n

    def __len__(self):
        """
        A delegator to give the length of the collection in data.
        """
        return len(self.data)

    def __getitem__(self, idx):
        """
        A delegator to get items from data.
        """
        return self.data[idx]

    def first_page(self):
        """
        :return: The first page of results.
        :rtype: PaginatedCollection
        Returns +self+ (and no API call is made) when already on the first page.

        >>> alerts.current_page_number # => 5
        >>> first_page = alerts.first_page
        >>> alerts.current_page_number # => 5
        >>> first_page.current_page_number # => 1
        """
        if self.has_previous_page:
            return self._updated_collection({'number': 1})
        else:
            return self

    def previous_page(self):
        """
        :return: The previous page of results.
        :rtype: PaginatedCollection
        Returns +self+ (and no API call is made) when already on the first page.

        >>> alerts.current_page_number # => 5
        >>> previous_page = alerts.previous_page
        >>> alerts.current_page_number # => 5
        >>> previous_page.current_page_number # => 4
        """
        if self.has_previous_page:
            return self._updated_collection(self._previous_page_params)
        else:
            return self

    def next_page(self):
        """
        :return: The next page of results.
        :rtype: PaginatedCollection
        Returns +self+ (and no API call is made) when already on the last page.

        >>> alerts.current_page_number # => 5
        >>> next_page = alerts.next_page
        >>> alerts.current_page_number # => 5
        >>> next_page.current_page_number # => 6
        """
        if self.has_next_page:
            return self._updated_collection(self._next_page_params)
        else:
            return self

    def last_page(self):
        """
        :return: The last page of results.
        :rtype: PaginatedCollection
        Returns +self+ (and no API call is made)  when already on the last page.

        >>> alerts.current_page_number # => 5
        >>> last_page = alerts.last_page
        >>> alerts.current_page_number # => 5
        >>> last_page.current_page_number # => 25
        """
        if not self.is_last_page:
            return self._updated_collection(self._last_page_params)
        else:
            return self

    def page(self, page_number=None):
        """
        :return: The +page_number+ page of data.
        :rtype: PaginatedCollection
        Returns +self+ when +page_number+ == +#current_page_number+

        :param int page_number: The page number of the data wanted.
            Must be between 1 and +#last_page_number+. (required)
        :raise ValueError if no page number or an out-of-bounds page number is supplied.
        >>> alerts.current_page_number # => 5
        >>> page = alerts.page(2)
        >>> alerts.current_page_number # => 5
        >>> page.current_page_number # => 2
        """
        if page_number is None:
            raise ValueError('You must supply a page number.')
        if int(page_number) < 1:
            raise ValueError('Page number cannot be less than 1.')
        if int(page_number) > int(self.last_page_number):
            raise ValueError('Page number cannot be greater than the last page number.')

        if int(page_number) != int(self.current_page_number):
            return self._updated_collection({'number': str(page_number), 'size': (self._next_page_params or self._previous_page_params)['size']})
        else:
            return self

    @property
    def current_page_number(self):
        """
        :return: The current page number of data.
        :rtype: str
        """
        previous = self.previous_page_number
        page = '1'
        if previous:
            page = str(int(previous) + 1)
        return page

    @property
    def previous_page_number(self):
        """
        :return: The previous page number of data.
        :rtype: str, None
        """
        return self._previous_page_params.get('number', None)

    @property
    def next_page_number(self):
        """
        :return: The next page number of data.
        :rtype: str, None
        """
        return self._next_page_params.get('number', None)

    @property
    def last_page_number(self):
        """
        :return: The previous page number of data.
        :rtype: str, None
        """
        return self._last_page_params.get('number', None)

    @property
    def has_previous_page(self):
        """
        :return: Whether or not there is a previous page of data in the collection.
        :rtype: bool
        """
        return self.previous_page_number is not None

    @property
    def has_next_page(self):
        """
        :return: Whether or not there is a next page of data in the collection.
        :rtype: bool
        """
        return self.next_page_number is not None

    @property
    def is_last_page(self):
        """
        :return: Whether or not the collection is on the last page.
        :rtype: bool
        """
        return self.last_page_number is None

    @property
    def _next_page_params(self):
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
    def _previous_page_params(self):
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
    def _last_page_params(self):
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

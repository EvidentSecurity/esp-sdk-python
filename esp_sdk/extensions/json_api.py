from __future__ import absolute_import


from six import iteritems
from six.moves.urllib.parse import parse_qs, urlparse

from .utilities import singularize

import re


class JsonApi(object):
    """
    NOTE: This class transforms the json api formated api response into a format
    friendler to the models with associated data from included
    """

    def __init__(self, json_api_dict):
        self.json_api_dict = json_api_dict

    def convert(self):
        included = self.json_api_dict.get('included', None)
        if included:
            del self.json_api_dict['included']
        data = self.json_api_dict.get('data', {})
        if isinstance(data, list):
            converted_data = [self.__parse_object(o, included) for o in data]
            self.json_api_dict['data'] = converted_data
        else:
            self.json_api_dict.update(self.__parse_object(data, included))

        return self.json_api_dict

    def __parse_object(self, object, included=None):
        if not isinstance(object, list) and not isinstance(object, dict):
            return object
        merged = self.__merge_attributes(object)
        merged.update(self.__parse_elements(merged))
        merged.update(self.__parse_relationships(merged, included))
        return merged

    def __merge_attributes(self, object):
        if isinstance(object, dict):
            if 'attributes' in object:
                merged = dict(object, **object['attributes'])
                del merged['attributes']
                return merged
        return object

    def __parse_elements(self, object):
        elements = {}
        for a, v in iteritems(object):
            if isinstance(v, dict):
                elements[a] = self.__parse_object(v)
            elif isinstance(v, list):
                elements[a] = [self.__parse_object(o) for o in v]
            else:
                elements[a] = v
        return elements

    def __parse_relationships(self, object, included):
        relationships = object.get('relationships', None)
        if not relationships:
            return {}
        for assoc, details in iteritems(relationships):
            object.update(self.__extract_foreign_keys(assoc, details))
            object.update(self.__merge_included_objects(assoc, details.get('data', None), included))
        return object

    def __extract_foreign_keys(self, assoc, assoc_details):
        data = assoc_details.get('data', None)
        related_link = assoc_details.get('links', {}).get('related', {})
        if data:
            return self.__parse_data(assoc, data)
        elif related_link:
            return self.__parse_related_link(assoc, related_link)
        return {}

    def __parse_data(self, assoc, data):
        if isinstance(data, list):
            return {singularize(assoc) + "_ids": [d.get('id', None) for d in data]}
        else:
            return {assoc + "_id": data.get('id', None)}

    def __parse_related_link(self, assoc, related_link):
        # parse the url to get the id if the data node is not returned
        id_re = re.compile('/(\d+)\.json\Z')
        id_match = id_re.search(related_link)
        if id_match:
            return {assoc + "_id": id_match.group(1)}

        # parse the query string for the ids
        url = urlparse(related_link)
        if url.query:
            query = parse_qs(url.query)
            ids = query.get('filter[id_in][]', None)
            if ids:
                return {singularize(assoc) + "_ids": ids}

        return {}

    def __merge_included_objects(self, assoc, data, included):
        if not included or not data:
            return {}
        if isinstance(data, list):
            return {assoc: self.__merge_nested_included_objects(object, data, included)}
        elif isinstance(data, dict):
            return {assoc: (self.__merge_nested_included_objects(object, [data], included) + [None])[0]}

    def __merge_nested_included_objects(self, object, data, included):
        assocs = []
        for i in included:
            if i is None:
                continue
            for d in data:
                if i['type'] == d['type'] and i['id'] == d['id']:
                    assocs.append(i)
        return [self.__parse_object(i, included) for i in assocs]

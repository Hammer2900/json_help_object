import os
import json
import pickle
import six
import uuid
import webbrowser
import yaml

from jsontraverse.parser import JsonTraverseParser
from pygments import highlight, lexers, formatters
from json2html import *


class PickleObjectHelpClass(object):
    def __init__(self, obj, *args, **kwargs):
        self.obj = obj
        self.save_path = '/tmp/obj__{}.pickle'

    def to_obj_save_pickle(self, file_name):
        full_name = self.save_path.format(file_name)
        with open(full_name, 'wb') as handle:
            pickle.dump(self.obj, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return full_name

    def to_obj_load_pickle(self, file_name):
        with open(self.save_path.format(file_name), 'rb') as handle:
            return pickle.load(handle)

    @staticmethod
    def to_obj_list_pickle(self):
        return ['/tmp/{}'.format(x) for x in os.listdir("/tmp/") if 'obj__' in x]

    def to_obj_clean_pickle(self):
        pass


class IterateObjectClass(object):
    def print_items_in_iterable_dict(self, iterable_dict):
        for key, value in iterable_dict.iteritems():
            if isinstance(value, dict) or isinstance(value, list):
                print(JsonObjectHelpClass(value).to_color())
            else:
                print('{} : --> {}'.format(key, value))

    def print_items_in_iterable_dict_table(self, iterable_dict):
        pass

    def print_items_in_iterable_list(self, iterable_list):
        pass

    def pickle_all_items_from_iterable(self):
        pass


class JsonObjectHelpClass(object):
    def __init__(self, data, *args, **kwargs):
        self.raw = data
        self.json = self._check_data_type(data)
        self._check_bin_attribute()

    def _check_data_type(self, data):
        if isinstance(data, str) or isinstance(data, six.string_types):
            return self._proccess_string(data)
        elif isinstance(data, dict) or isinstance(data, list):
            return self._proccess_json(data)
        else:
            raise Exception("Unknown data format.")

    def _check_bin_attribute(self):
        if isinstance(self.json, list):
            self.list_obj = [JsonObjectHelpClass(x) for x in self.json]
        else:
            for key, value in self.json.items():
                if isinstance(value, dict):
                    setattr(self, key, JsonObjectHelpClass(value))
                elif isinstance(value, list):
                    if self._list_check_type_simple(value):
                        setattr(self, key, value)
                    else:
                        setattr(self, key, [JsonObjectHelpClass(x) for x in value])
                else:
                    setattr(self, key, value)

    def _list_check_type_simple(self, data):
        if not data:
            return True
        elif isinstance(data[0], dict):
            return False
        else:
            return True

    def _proccess_json(self, data):
        return data

    def _proccess_string(self, data):
        return json.loads(data)

    def to_color(self, indent=3):
        return highlight(
            unicode(json.dumps(self.json, indent=indent), 'UTF-8'),
            lexers.JsonLexer(),
            formatters.TerminalFormatter()
        )

    def to_print(self, indent=3):
        print(json.dumps(self.json, indent=indent))

    def to_browser(self):
        full_name = '/tmp/to_browser_{}.html'.format(uuid.uuid4())
        with open(full_name, 'w') as f:
            f.write(json2html.convert(json=self.json))
        webbrowser.open('file://{}'.format(full_name))
        return 'file://{}'.format(full_name)

    def to_file_save(self, file_name, indent=3):
        with open(file_name, 'w') as f:
            f.write(json.dumps(self.json, indent=indent))

    def to_pickle_save(self, file_name):
        full_name = '/tmp/{}.pickle'.format(file_name)
        with open(full_name, 'wb') as handle:
            pickle.dump(self.json, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return full_name

    def parse_query(self, query):
        return JsonTraverseParser(unicode(self.raw)).traverse(query)

    @staticmethod
    def pickle_list():
        return ['/tmp/{}'.format(x) for x in os.listdir("/tmp/") if '.pickle' in x]

    @staticmethod
    def to_pickle_load(file_name):
        with open('/tmp/{}.pickle'.format(file_name), 'rb') as handle:
            return pickle.load(handle)

    def to_yaml(self):
        print(yaml.safe_dump(self.json, default_flow_style=False))


if __name__ == '__main__':
    s = '{"id": 1, "name": "A green door", "price": [{"id": 1, "name": "A green door", "price": 12.50, "tags": ["home", "green"]}, {"id": 1, "name": "A green door", "price": 12.50, "tags": ["home", "green"]}], "tags": {"name": "A green door"}}'
    # JsonObjectHelpClass(s).to_print(6)
    # print JsonObjectHelpClass(s).to_color()
    # JsonObjectHelpClass(s).to_yaml()
    # JsonObjectHelpClass(s).to_pickle_save('testname')
    # print JsonObjectHelpClass(s).to_browser()
    # print JsonObjectHelpClass('{}').pickle_list()
    # print JsonObjectHelpClass(s).parse_query(u'name')
    # print PickleObjectHelpClass(object).to_obj_save_pickle('dfdfdfdfdf')
    # print PickleObjectHelpClass(object).to_obj_load_pickle('dfdfdfdfdf')
    IterateObjectClass().print_items_in_iterable_dict(json.loads(s))




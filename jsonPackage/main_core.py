import os
import json
import pickle
import uuid
import webbrowser
import yaml

from jsontraverse.parser import JsonTraverseParser
from pygments import highlight, lexers, formatters
from json2html import *


class DirStatusClass(object):
    def __init__(self, obj, magic=None, sub=None):
        self.obj = obj
        self.magic = magic
        self.sub = sub
        self.result = {
            'magic': [],
            'hidden': [],
            'simple': [],
            'magic_count': 0,
            'simple_count': 0,
            'hidden_count': 0,
            'type': str(type(self.obj)),
            # 'dict': self.obj.__dict__
        }
        self.grab_info()

    @staticmethod
    def _header_print(name, line_count=30, field_char='='):
        return '{} {} {}'.format(field_char * line_count, name, field_char * line_count)

    def grab_info(self):
        for lines in dir(self.obj):
            if lines.startswith('__'):
                self.result['magic'].append(lines)
            elif lines.startswith('_'):
                self.result['hidden'].append(lines)
            else:
                self.result['simple'].append(lines)
        self.result['magic_count'] = len(self.result['magic'])
        self.result['simple_count'] = len(self.result['simple'])
        self.result['hidden_count'] = len(self.result['hidden'])

    def _print_sub_or(self, key, lines):
        if not self.sub:
            print(f'{key}. {lines}')
        else:
            print(f'{key}. {lines}')
            for sub in dir(getattr(self.obj, lines)):
                print('{}# {}'.format(' ' * 10, sub))

    def print_methods(self):
        if self.magic:
            print(self._header_print('MAGIC METHODS'))
            for key, lines in enumerate(self.result['magic'], start=1):
                self._print_sub_or(key, lines)
            print(self._header_print('HIDDEN METHODS'))
            for key, lines in enumerate(self.result['hidden'], start=1):
                self._print_sub_or(key, lines)
        print(self._header_print('METHODS'))
        for key, lines in enumerate(self.result['simple'], start=1):
            self._print_sub_or(key, lines)
        print(self._header_print('END'))

    def dict_with_methods(self):
        return self.result


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
    def to_obj_list_pickle():
        return ['/tmp/{}'.format(x) for x in os.listdir("/tmp/") if 'obj__' in x]

    def to_obj_clean_pickle(self):
        pass


class IterateObjectClass(object):
    def print_items_in_iterable_dict(self, iterable_dict):
        for key, value in iterable_dict.items():
            if isinstance(value, dict) or isinstance(value, list):
                print(JsonObjectHelpClass(value).to_print())
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
        if isinstance(data, str):
            return self._proccess_string(data)
        elif isinstance(data, dict) or isinstance(data, list):
            return self._proccess_json(data)
        else:
            return data

    def _check_bin_attribute(self):
        if isinstance(self.json, list):
            self.list_obj = [JsonObjectHelpClass(x) for x in self.json]
        elif isinstance(self.json, dict):
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
        try:
            return json.loads(data)
        except:
            return data

    def to_color(self, indent=3):
        return highlight(
            json.dumps(self.json, indent=indent), 'UTF-8',
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
        return JsonTraverseParser(self.raw).traverse(query)

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
    # IterateObjectClass().print_items_in_iterable_dict(json.loads(s))
    # JsonObjectHelpClass([1,2]).to_print()
    JsonObjectHelpClass(['qwerqwe', 'qweqwe']).to_print()


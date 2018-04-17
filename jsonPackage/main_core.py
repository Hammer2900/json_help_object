import json
import pickle
import webbrowser
import yaml
from pygments import highlight, lexers, formatters


class JsonObjectHelpClass(object):
    def __init__(self, data, *args, **kwargs):
        self.raw = data
        self.json = self._check_data_type(data)
        self._check_bin_attribute()

    def _check_data_type(self, data):
        if isinstance(data, str) or isinstance(data, unicode):
            return self._proccess_string(data)
        elif isinstance(data, dict):
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

    def _color(self, indent=3):
        return highlight(
            unicode(json.dumps(self.json, indent=indent), 'UTF-8'),
            lexers.JsonLexer(),
            formatters.TerminalFormatter()
        )

    def _proccess_json(self, data):
        return data

    def _proccess_string(self, data):
        return json.loads(data)

    def to_print(self, indent=3):
        print(json.dumps(self.json, indent=indent))

    def to_browser(self):
        webbrowser.open_new_tab('http://jsoneditoronline.org/?json={}'.format(self.json))

    def to_file_save(self, file_name, indent=3):
        with open(file_name, 'w') as f:
            f.write(json.dumps(self.json, indent=indent))

    def to_pickle_save(self, file_name):
        with open('/tmp/{}.pickle'.format(file_name), 'wb') as handle:
            pickle.dump(self.json, handle, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def to_pickle_load(file_name):
        with open('/tmp/{}.pickle'.format(file_name), 'wb') as handle:
            return pickle.load(handle)

    def to_yaml(self):
        print yaml.safe_dump(self.json, default_flow_style=False)


if __name__ == '__main__':
    s = '{"id": 1, "name": "A green door", "price": [{"id": 1, "name": "A green door", "price": 12.50, "tags": ["home", "green"]}, {"id": 1, "name": "A green door", "price": 12.50, "tags": ["home", "green"]}], "tags": {"name": "A green door"}}'
    # JsonObjectHelpClass(s).to_print(6)
    print JsonObjectHelpClass(s)._color()
    # JsonObjectHelpClass(s).to_yaml()
    # JsonObjectHelpClass(s).to_pickle_save('testname')
    # JsonObjectHelpClass(s).browser()



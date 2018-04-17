import json
import webbrowser


class JsonObjectHelpClass(object):
    def __init__(self, data, *args, **kwargs):
        self.json = self._check_data_type(data)
        self._check_bin_attribute()

    def _check_data_type(self, data):
        if isinstance(data, str):
            return self._proccess_string(data)
        elif isinstance(data, dict):
            return self._proccess_json(data)
        else:
            raise Exception("Unknown data format.")

    def _check_bin_attribute(self):
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

    def pprint(self, indent=3):
        print(json.dumps(self.json, indent=indent))

    def browser(self):
        webbrowser.open_new_tab('http://jsoneditoronline.org/?json={}'.format(self.json))


if __name__ == '__main__':
    s = '{"id": 1, "name": "A green door", "price": [{"id": 1, "name": "A green door", "price": 12.50, "tags": ["home", "green"]}, {"id": 1, "name": "A green door", "price": 12.50, "tags": ["home", "green"]}], "tags": {"name": "A green door"}}'
    # JsonObjectHelpClass(s).print(6)
    # JsonObjectHelpClass(s).browser()


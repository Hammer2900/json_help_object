import json


class JsonObjectHelpClass(object):
    def __init__(self, data, *args, **kwargs):
        self.json = self._check_data_type(data)
        self.bin = self._check_bin_attribute(data)

    def _check_data_type(self, data):
        if isinstance(data, str):
            return self._proccess_string(data)
        elif isinstance(data, dict):
            return self._proccess_json(data)
        else:
            raise Exception("Unknown data format.")

    def _check_bin_attribute(self, data):
        return None

    def _proccess_json(self, data):
        return data

    def _proccess_string(self, data):
        return json.loads(data)

    def print(self, indent=3):
        print(json.dumps(self.json, indent=indent))


if __name__ == '__main__':
    s = '{"id": 1, "name": "A green door", "price": 12.50, "tags": ["home", "green"]}'
    a = JsonObjectHelpClass(s)
    print('Debug -->', a.json)
    a.print(5)

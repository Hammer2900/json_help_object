==========================================
Welcome to json help object and functions.
==========================================

I create this package for help see or debug json in my test scripts or projects.
Beware this is slow realization for personal use.

Install
-------

pip install git+https://github.com/Hammer2900/json_help_object --upgrade

Example json
-------

from jsonPackage.fast_utils import *

example_json= '{"id": 1, "name": "A green door", "price": 12.50, "tags": ["home", "green"]}'

jcolor(example_json)

jprint(example_json)

jspickle(example_json)

jlpickle(example_json)

jyaml(example_json)

j2html(example_json)

pickle_list()

jquery(example_json, 'name')

Example object
-------

from jsonPackage.fast_utils import ospickle, olpickle

ospickle('team009', object)

obj = olpickle('team009')

Example list
-------

list_iter_print(json.loads(example_json))


Example dir
-------

dir_print(os)
dir_html(os)


Example help time function
-------

@timeit
def new_replica_call():
    pass
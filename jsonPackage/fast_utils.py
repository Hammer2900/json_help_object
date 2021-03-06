from __future__ import absolute_import
from .main_core import *
from .log_function import *


def jprint(dict_json, indent=6):
    print(JsonObjectHelpClass(dict_json).to_print(indent))


def jcolor(dict_json, indent=6):
    print(JsonObjectHelpClass(dict_json).to_color(indent))


def jspickle(dict_json, file_name):
    JsonObjectHelpClass(dict_json).to_pickle_save(file_name)


def jquery(dict_json, query):
    """
    Example "name.cool.0.dict"
    :param dict_json:
    :param query: list []
    """
    return JsonObjectHelpClass(dict_json).parse_query(query)


def jlpickle(file_name):
    return JsonObjectHelpClass('{}').to_pickle_load(file_name)


def pickle_list():
    return JsonObjectHelpClass('{}').pickle_list()


def jyaml(dict_json):
    print(JsonObjectHelpClass(dict_json).to_yaml())


def j2html(dict_json):
    print(JsonObjectHelpClass(dict_json).to_browser())


def ospickle(file_name, obj):
    return PickleObjectHelpClass(obj).to_obj_save_pickle(file_name)


def olpickle(file_name):
    return PickleObjectHelpClass(object).to_obj_load_pickle(file_name)


def obj_pickle_list():
    """
    Show list pickle objects.
    """
    return PickleObjectHelpClass(object).to_obj_list_pickle()


def ocpickle():
    """
    Clean temp folder.
    :rtype: object
    """
    pass


def list_iter_print(iterable_dict):
    IterateObjectClass().print_items_in_iterable_dict(iterable_dict)


def dir_print(obj, magic=False, sub=False):
    DirStatusClass(obj, magic, sub).print_methods()


def dir_html(obj, magic=False, sub=False):
    print(JsonObjectHelpClass(DirStatusClass(obj, magic, sub).dict_with_methods()).to_browser())


def obj_size(obj, info=False):
    PythonProfile().calculate_obj_size(obj, info)


log = log_exceptions  # decorator
pc = parallel_calculation  # function

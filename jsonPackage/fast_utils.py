from __future__ import absolute_import
from .main_core import *


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
    pass


def ocpickle():
    """
    Clean temp folder.
    :rtype: object
    """
    pass


def list_iter_print(iterable_dict):
    IterateObjectClass().print_items_in_iterable_dict(iterable_dict)

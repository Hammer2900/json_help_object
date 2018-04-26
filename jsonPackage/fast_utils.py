from main_core import *


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
    print JsonObjectHelpClass(dict_json).to_browser()


def ospickle():
    pass


def olpickle():
    pass

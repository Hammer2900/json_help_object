from main_core import *


def jprint(dict_json, indent=6):
    print(JsonObjectHelpClass(dict_json).to_print(indent))


def jcolor(dict_json, indent=6):
    print(JsonObjectHelpClass(dict_json).to_color(indent))


def jspickle(dict_json, file_name):
    JsonObjectHelpClass(dict_json).to_pickle_save(file_name)


def jlpickle(file_name):
    return JsonObjectHelpClass('{}').to_pickle_load(file_name)


def pickle_list():
    return JsonObjectHelpClass('{}').pickle_list()


def jyaml(dict_json):
    print yaml.safe_dump(dict_json, default_flow_style=False)


def j2html(dict_json):
    print JsonObjectHelpClass(dict_json).to_browser()

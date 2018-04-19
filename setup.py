
from setuptools import setup, find_packages

setup(
    name='python_json_help_object',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Json helper class for debug.',
    long_description=open('README.rst').read(),
    install_requires=['pygments', 'pyyaml', 'json2html', 'json-traverse'],
    url='https://github.com/Hammer2900/json_help_object',
    author='Jek Hammer',
    author_email='evgeny2900@gmail.com'
)

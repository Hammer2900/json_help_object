import json
import os
from unittest.mock import patch
import pytest
from jsonPackage.fast_utils import *

# Example JSON used for all tests
EXAMPLE_JSON_STR = (
    '{"id": 1, "name": "A green door", "price": 12.50, "tags": ["home", "green"], "nested": {"value": 42}}'
)
EXAMPLE_JSON_DICT = json.loads(EXAMPLE_JSON_STR)
TEST_PICKLE_FILENAME = 'gemini_test_pickle'


@pytest.fixture(scope='function', autouse=True)
def cleanup_temp_files():
    """This fixture runs after each test function to clean up created files."""
    yield
    # Cleanup pickle files
    pickle_path = f'/tmp/{TEST_PICKLE_FILENAME}.pickle'
    if os.path.exists(pickle_path):
        os.remove(pickle_path)

    # Cleanup HTML files
    html_path = '/tmp/to_browser_test-uuid.html'
    if os.path.exists(html_path):
        os.remove(html_path)


def test_jquery():
    """Tests the jquery function for correctness."""
    # Test a simple key
    assert jquery(EXAMPLE_JSON_STR, 'name') == 'A green door'

    # Test a nested key
    assert jquery(EXAMPLE_JSON_STR, 'nested.value') == 42

    # Test an element in a list
    assert jquery(EXAMPLE_JSON_STR, 'tags.0') == 'home'

    # Test a non-existent key (should return None based on library behavior)
    # Note: jsontraverse returns None for missing keys.
    assert jquery(EXAMPLE_JSON_STR, 'nonexistent.key') is None


def test_pickle_save_and_load():
    """
    Tests that jspickle saves and jlpickle loads data correctly.
    Note: This test writes to the /tmp/ directory due to hardcoded paths in the library.
    """
    # Save the JSON object to a pickle file
    jspickle(EXAMPLE_JSON_DICT, TEST_PICKLE_FILENAME)

    # Check that the file was actually created
    assert os.path.exists(f'/tmp/{TEST_PICKLE_FILENAME}.pickle')

    # Load the data back from the pickle file
    loaded_data = jlpickle(TEST_PICKLE_FILENAME)

    # Assert that the loaded data is identical to the original
    assert loaded_data == EXAMPLE_JSON_DICT


def test_jprint(capsys):
    """Tests that jprint outputs correct, parsable JSON to stdout."""
    jprint(EXAMPLE_JSON_DICT)
    captured = capsys.readouterr()

    # Check that the output is not empty
    assert captured.out.strip() != ''

    # Check that the output can be parsed as JSON and is equivalent to the input
    loaded_from_out = json.loads(captured.out)
    assert loaded_from_out == EXAMPLE_JSON_DICT


def test_jyaml(capsys):
    """Tests that jyaml outputs correct YAML to stdout."""
    jyaml(EXAMPLE_JSON_DICT)
    captured = capsys.readouterr()

    # Check for key elements of the YAML structure in the output
    assert 'name: A green door' in captured.out
    assert 'nested:' in captured.out
    assert '  value: 42' in captured.out
    assert '- home' in captured.out
    assert '- green' in captured.out


# @patch('webbrowser.open')
# @patch('uuid.uuid4', return_value='test-uuid')
# def test_j2html(mock_uuid, mock_webbrowser_open):
#     """
#     Tests that j2html creates an HTML file and attempts to open it
#     without actually opening a browser.
#     """
#     returned_uri = j2html(EXAMPLE_JSON_DICT)
#
#     # Define the expected raw path and the expected URI
#     expected_raw_path = '/tmp/to_browser_test-uuid.html'
#     expected_uri = f'file://{expected_raw_path}'
#
#     # Check that the returned value is the URI
#     assert returned_uri == expected_uri
#
#     # Check that webbrowser.open was called with the correct URI
#     mock_webbrowser_open.assert_called_once_with(expected_uri)
#
#     # Check that the file was created using the RAW path
#     assert os.path.exists(expected_raw_path)
#     with open(expected_raw_path, 'r') as f:
#         content = f.read()
#         assert '<table>' in content
#         assert 'A green door' in content
#         assert '42' in content


def test_dir_print(capsys):
    """Tests the dir_print function to ensure it prints object methods."""
    # We test it on a simple, well-known object like 'os'
    dir_print(os)
    captured = capsys.readouterr()

    # Check for the header and some known methods/attributes of the 'os' module
    assert 'METHODS' in captured.out
    assert 'listdir' in captured.out
    assert 'path' in captured.out
    assert 'system' in captured.out

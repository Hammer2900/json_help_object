# Project Overview

This project is a Python library called `json_help_object` designed to assist with debugging and manipulating JSON objects. It provides a collection of utility functions to format, convert, and inspect JSON data, making it easier to work with complex JSON structures during development and testing.

The core of the library is the `JsonObjectHelpClass`, which wraps a JSON object (or a string that can be parsed into one) and exposes methods for various operations. The library also includes helper classes and functions for inspecting Python objects, profiling memory usage, and performing parallel computations.

## Main Technologies

*   **Language:** Python
*   **Key Libraries:**
    *   `pygments`: For colorizing JSON output.
    *   `pyyaml`: For converting JSON to YAML.
    *   `json2html`: For converting JSON to HTML.
    *   `jsontraverse`: For querying JSON objects.
    *   `pympler`: For calculating the size of Python objects.

# Building and Running

This is a Python library, so there is no separate build process. It can be installed directly from the GitHub repository.

## Installation

To install the library, use the following pip command:

```bash
pip install git+https://github.com/Hammer2900/json_help_object --upgrade
```

## Running Tests

The project includes a `tests` directory, but there are no explicit test commands defined in the project's configuration. To run the tests, you can use `pytest`:

```bash
pytest
```

*TODO: Add a dedicated test script to the project configuration (e.g., in a `Makefile` or as a script in `Pipfile`).*

# Development Conventions

## Code Style

The code follows standard Python conventions (PEP 8), although there is no linter configuration file (e.g., `.pylintrc`, `pyproject.toml`) included in the project.

## Testing

The project has a `tests` directory containing a `test.py` file. This indicates that testing is a part of the development process, but the test coverage is not specified.

## Contribution

There are no explicit contribution guidelines in the repository.

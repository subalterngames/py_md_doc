# PyMdDoc

Generate markdown documentation for your Python scripts' code comments that is compatible with GitHub. It's like Sphinx, but with simpler requirements and results. It's also not as flexible as Sphinx and is mainly useful for scripts containing only a few classes.

For example output, [see the code documentation for this module](https://github.com/subalterngames/py_md_doc/blob/main/docs/py_md_doc.md).

## Installation

```bash
pip3 install py-md-doc
```

## Usage


### 1. Documentation for this module

1. Clone this repo.
2. `cd path/to/py_md_doc` (Replace `path_to`) with the actual path to this repo.)
3. `python3 doc_gen.py`

### 2. Documentation for your own module

```python
from py_md_doc import PyMdDoc
from pathlib import Path


md = PyMdDoc(input_directory=Path("my_module/my_module"), files=["my_script.py"], metadata_path="metadata.json")
md.get_docs(output_directory=Path("my_module/docs"))
```

**For the API, [read this](https://github.com/subalterngames/py_md_doc/blob/main/docs/py_md_doc.md).**

### 3. Documentation with class inheritance

1. Generate documentation for each child script (see above).
2. Use [`ClassInheritance`](https://github.com/subalterngames/py_md_doc/blob/main/docs/class_inheritance.md) to append inherited fields, functions, etc. from the generated documents.

## Code comments format

- One class per file.
- Class descriptions begin and end with `"""` immediately after the class definition.
- Class variables begin with `""":class_var` and end with `"""` and must be before the constructor declaration. The line immediately after them is the variable declaration.
- Fields begin with `""":field` and end with `"""` in the constructor. The line immediately after them is the field declaration.
- Function descriptions begin and end with `"""` immediately after the function definition.
  - Function parameter descriptions are lines within the function description that begin with `:param`
  - Function return description are lines within the function description that begin with `:return:`
- Function names that begin with `_` are ignored.
- The code for PyMdDoc as well as the code examples below use [type hinting](https://docs.python.org/3/library/typing.html). You do _not_ need type hinting in your code for PyMdDoc to work properly.

```python
class MyClass:
    """
    This is the class description.
    """

    """:class_var
    This is a class variable.
    """
    CLASS_VAR: int = 0

    def __init__(self):
        """field:
        The ID of this object.
        """
        self.val = 0

    def set_val(self, val: int) -> None:
        """
        Set the val of this object.

        :param val: The new value.
        """

        self.val = val

    def get_val(self) -> int:
        """
        :return The value of this object.
        """
        
        return self.val

    def _private_function(self) -> None:
        """
        This won't appear in the documentation.
        """

        return
```

- [Enum values](https://docs.python.org/3/library/enum.html) are documented by commenting the line next to them.

```python
from enum import Enum

class MyEnum(Enum):
    a = 0  # The first value.
    b = 1  # The second value.
```

## Metadata file

You can add an optional metadata dictionary (see [the constructor](https://github.com/subalterngames/py_md_doc/blob/main/docs/py_md_doc.md#__init__)).

A metadata file is structured like this:

```json
{
  "PyMdDoc":
  {
    "Constructor": {
      "description": "",
      "functions": ["__init__"]
    },
    "Documentation Generation": {
      "description": "Use these functions to generate your documentation.",
      "functions": ["get_docs", "get_doc"]
    },
    "Helper Functions": {
      "description": "These functions are used in `get_docs()`. You generally won't need to call these yourself.",
      "functions": ["get_class_description", "get_class_variables", "get_function_documentation", "get_enum_values", "get_fields"]
    }
  }
}
```

- The top-order key of the dictionary (`"PyMdDoc"`) is the name of the class. You don't need to add every class that you wish to document. If the class is not listed in `metadata.json` but is listed in the `files` parameter, its functions will be documented in the order they appear in the script.
- Each key in the class metadata (`"Constructor"`, `"Documentation Generation"`, `"Helper Functions"`) is a section.
  - Each section name will be a header in the document, except for `"Constructor"` and `"Ignore"`.
  - Any function in the `"Ignore"` category won't be documented.
  - Each section has a `"description"` and a list of names of `"functions"`. The functions will appear in the section in the order they appear in this list.
- If the class name is listed in `metadata.json` and a function name can't be found in any of the section lists, the console will output a warning. For example, if you were to add a function named `new_function()` to `PyMdDoc`, you'd have to add it to a section in the metadata file as well because `PyMdDoc` is a key in the metadata dictionary.

## Limitations

- This script is for class objects only and won't document functions that aren't in classes:

```python
def my_func():
    """
    This function will be ignored.
    """
    pass 

class MyClass:
    """
    This class will be in the documentation.
    """

    def class_func(self):
        """
        This function will be in the documentation.
        """
        pass

def another_my_func():
    """
    This function will be erroneously included with MyClass.
    """
    pass 
```

- Functions can be grouped and reordered into categories, but classes and fields are always documented from the top of the document to the bottom:

```python
class MyClass:
    """
    This class will documented first.
    """

    def class_func(self):
        """
        This function will be documented first.
        """
        pass

    def another_class_func(self):
        """
        This function will be documented second.
        """
        pass

class AnotherClass:
    """
    This class will be documented second.
    """
```

## `VarDoc`

To create API documentation for a script that contains only variables (no classes or functions), use [`VarDoc`](https://github.com/subalterngames/py_md_doc/blob/main/docs/var_doc.md).

# Changelog

See [changelog](docs/changelog.md).
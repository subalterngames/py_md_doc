# PyMdDoc

`from py_md_doc import PyMdDoc`

Generate Markdown documentation for your Python scripts.

```python
from pathlib import Path
from py_md_doc import PyMdDoc

if __name__ == "__main__":
    md = PyMdDoc(input_directory=Path("."),
                 files=["py_md_doc/py_md_doc.py", "py_md_doc/parameter.py"],
                 metadata_path="metadata.json")
    md.get_docs(output_directory=Path("docs"))
```

***

## Class Variables

| Variable | Type | Description | Value |
| --- | --- | --- | --- |
| `CLASS_VAR` | int | This is a test class variable. It doesn't do anything in this code other than test that the documentation generates correctly. | `0` |

***

## Fields

- `files` The root directory of the source .py files.

- `root_import_name` The expected name of the root import name, derived the input directory.

- `special_imports` A list of special import statements from `__init__.py`

- `metadata` The metadata dictionary loaded from the metadata file. If there is no metadata file, this is empty.

***

## Functions

#### \_\_init\_\_

**`PyMdDoc(input_directory, files)`**

**`PyMdDoc(input_directory, files, metadata_path=None)`**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| input_directory |  Union[Path, str] |  | The path to the root input directory for the Python scripts. Can be a `Path` or `str`. |
| files |  List[str] |  | A list of Python script filenames relative to `input_directory`. This script will generate documentation only for these files. |
| metadata_path |  Union[Path, str] | None | The path to the metadata file. Can be None. See the README for how to format this file. |

***

### Documentation Generation

Use these functions to generate your documentation.

#### get_doc

**`self.get_doc(file)`**

**`self.get_doc(file, import_prefix=None)`**

Create a document from a Python file with the API for each class. Returns the document as a string.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| file |  Path |  | The path to the Python script. |
| import_prefix |  str  | None | If not None, replace the import prefix with this import prefix. |

#### get_docs

**`self.get_docs(output_directory)`**

**`self.get_docs(output_directory, import_prefix=None)`**

Generate documents for all the Python files and write them to disk.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| output_directory |  Union[Path, str] |  | The path to the output directory. Can be of type `Path` or `str`. |
| import_prefix |  str  | None | If not None, replace the import prefix with this import prefix. |

#### get_doc_toc

**`PyMdDoc.get_doc_toc(doc)`**

_(Static)_


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| doc |  str |  | The document. |

_Returns:_  The table of contents of the document.

#### get_dir_toc

**`PyMdDoc.get_dir_toc(directory, import_prefix, link_prefix)`**

**`PyMdDoc.get_dir_toc(directory, import_prefix, link_prefix, class_name_overrides=None)`**

_(Static)_


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| directory |  Union[str, Path] |  | The root directory of the documentation. |
| import_prefix |  str |  | The base import prefix (usually the name of the module). |
| link_prefix |  str |  | The prefix for all links. |
| class_name_overrides |  Dict[str, str] | None | Class name overrides for cases where the file underscore_name doesn't match UnderscoreName. Key = The expected bad class name. Value = The corrected name. |

_Returns:_  The table of contents of the documentation files in the directory.

***

### Helper Functions

These functions are used in `get_docs()`. You generally won't need to call these yourself.

#### get_class_description

**`PyMdDoc.get_class_description(file_txt)`**

_(Static)_

Parses a file starting at a line defined by start_index to get the class name and description.
This assumes that the class has a triple quote description.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| file_txt |  str |  | All of the text of the file. |

#### get_class_variables

**`PyMdDoc.get_class_variables(lines, start_index)`**

_(Static)_


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| lines |  List[str] |  | All of the lines of the file. |
| start_index |  int |  | Start looking for fields at this line. |

_Returns:_  A table of class variables as a string.

#### get_function_documentation

**`PyMdDoc.get_function_documentation(lines, start_index, class_name)`**

_(Static)_

Create documentation for a function and its parameters.


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| lines |  List[str] |  | The lines of the Python script. |
| start_index |  int |  | Start at this line to search for function documentation. |
| class_name |  str |  | The name of the class. Used for static function documentation. |

_Returns:_  The function documentation string.

#### get_enum_values

**`PyMdDoc.get_enum_values(lines, start_index)`**

_(Static)_

Returns a list of enum values.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| lines |  List[str] |  | The lines in the document. |
| start_index |  int |  | The line of the class defintion. |

#### get_fields

**`PyMdDoc.get_fields(lines, start_index)`**

_(Static)_

Get the field descriptions for this class.


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| lines |  List[str] |  | All of the lines of the file. |
| start_index |  int |  | Start looking for fields at this line. |

_Returns:_  A string of field documentation.

***


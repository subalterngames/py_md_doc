# PyMdDoc

`from  import PyMdDoc`

Generate Markdown documentation for your Python scripts.

```python
from py_md_doc import PyMdDoc
from pathlib import Path

# Generates the documentation for the py_md_doc module.
md = PyMdDoc(input_directory=Path("."), files=["py_md_doc.py"], metadata_path="metadata.json")
md.get_docs(output_directory=Path("../doc"))
```

***

## Fields

- `files` A list of paths to each Python script file as `Path` objects.

- `metadata` The metadata dictionary loaded from the metadata file. If there is no metadata file, this is empty.

- `root_import_name` The expected name of the root import name, derived the input directory.

```python
from py_md_doc import PyMdDoc
from pathlib import Path

# Generates the documentation for the py_md_doc module.
md = PyMdDoc(input_directory=Path("my_module"), files=["my_file.py"])
print(md.root_import_name) # my_module
```

- `special_imports` A list of special import statements from `__init__.py`

***

## Functions

#### \_\_init\_\_

**`def __init__(self, input_directory: Union[Path, str], files: List[str], metadata_path: Union[Path, str] = None)`**

| Parameter | Description |
| --- | --- |
| input_directory | The path to the root input directory for the Python scripts. Can be a `Path` or `str`. |
| files | A list of Python script filenames relative to `input_directory`. This script will generate documentation only for these files. |
| metadata_path | The path to the metadata file. Can be None. See the README for how to format this file. |

***

### Documentation Generation

_Use these functions to generate your documentation._

#### get_docs

**`def get_docs(self, output_directory: Union[Path, str]) -> None`**

Generate documents for all of the Python files and write them to disk.

| Parameter | Description |
| --- | --- |
| output_directory | The path to the output directory. Can be of type `Path` or `str`. |

#### get_doc

**`def get_doc(self, file: Path) -> str`**

Create a document from a Python file with the API for each class. Returns the document as a string.

| Parameter | Description |
| --- | --- |
| file | The path to the Python script. |

***

### Helper Functions

_These functions are used in `get_docs()`. You generally won't need to call these yourself._

#### get_fields

**`def get_fields(lines: List[str], start_index: int) -> str`**

_This is a static function._

Get the field descriptions for this class.


| Parameter | Description |
| --- | --- |
| lines | All of the lines of the file. |
| start_index | Start looking for fields at this line. |

_Returns:_  A string of field documentation.

#### get_class_description

**`def get_class_description(file_txt: str, lines: List[str], start_index: int) -> str`**

_This is a static function._

Parses a file starting at a line defined by start_index to get the class name and description.
This assumes that the class has a triple quote description.

| Parameter | Description |
| --- | --- |
| file_txt | All of the text of the file. |
| lines | All of the lines in the file. |
| start_index | The start index of the class declaration. |

#### get_function_documentation

**`def get_function_documentation(lines: List[str], start_index: int) -> str`**

_This is a static function._

Create documentation for a function and its parameters.


| Parameter | Description |
| --- | --- |
| lines | The lines of the Python script. |
| start_index | Start at this line to search for function documentation. |

_Returns:_  The function documentation string.

#### get_enum_values

**`def get_enum_values(lines: List[str], start_index: int) -> str`**

_This is a static function._

Returns a list of enum values.

| Parameter | Description |
| --- | --- |
| lines | The lines in the document. |
| start_index | The line of the class defintion. |

***


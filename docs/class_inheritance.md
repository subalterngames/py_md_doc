# ClassInheritance

`from py_md_doc import ClassInheritance`

Handle documentation with class inheritance.

***

#### get_from_directory

**`ClassInheritance.get_from_directory(input_directory, output_directory, import_path)`**

**`ClassInheritance.get_from_directory(input_directory, output_directory, import_path, overrides=None, import_prefix=None, excludes=None, includes=None)`**

_(Static)_

Generate documentation with class inheritance from a source directory.
This assumes that:

1. The entire hierarchy is in the same directory; anything outside of it will be ignored.
2. Each .py file is named with underscore snake casing and contains an uppercase camelcase class name, for example `my_class.py` and `MyClass`.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| input_directory |  Union[str, Path] |  | The input source directory of .py scripts. |
| output_directory |  Union[str, Path] |  | The output destination directory of .md files. |
| import_path |  str |  | The expected Python import path, for example `module.sub_module`. |
| overrides |  Dict[str, str] | None | Override any unexpected classes or filenames. Key = What would be programatically expected such as `MyClass`. Value = What actually exists such as `MYCLASS`. |
| import_prefix |  str  | None | The import prefrix, for example `from module.sub_module`. |
| excludes |  List[str] | None | Exclude any .py in this list. |
| includes |  List[str] | None | If not None, only include these .py files. |

#### get_from_type

**`ClassInheritance.get_from_type(t, directory)`**

**`ClassInheritance.get_from_type(t, directory, overrides=None)`**

_(Static)_

Generate documentation with class inheritance from a source type and documentation directory.

This assumes that:

1. Documentation without inheritance has already been generated (see `PyMdDoc.get_docs()`).
2. Type `t` is one of the classes in the .md `directory`.


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| t |  Type |  | The class type. |
| directory |  Union[str, Path] |  | The directory of output .md files that have already been generated. |
| overrides |  Dict[str, str] | None | Override any unexpected classes or filenames. Key = What would be programatically expected such as `MyClass`. Value = What actually exists such as `MYCLASS`. |

_Returns:_  Documentation text.

#### get_from_text

**`ClassInheritance.get_from_text(child_text, parent_texts)`**

_(Static)_

Generate documentation with inheritance from parent documentation.


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| child_text |  str |  | The documentation of the child class. |
| parent_texts |  List[str] |  | A list of documentation of the parent classes in order of inheritance. |

_Returns:_  An updated version of `child_text` that includes class inheritance.


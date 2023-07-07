# DocBase

`from py_md_doc.doc_base import DocBase`

Abstract base document generator class.

***

## Fields

- `metadata` The metadata dictionary loaded from the metadata file. If there is no metadata file, this is empty.

***

## Functions

#### \_\_init\_\_

**`DocBase()`**

**`DocBase(metadata_path=None)`**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| metadata_path |  Union[Path, str] | None | The path to the metadata file. Can be None. See the README for how to format this file. |

#### sort_by_metadata

**`self.sort_by_metadata(class_name, doc)`**

Sort a document's contents using `self.metadata`.


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| class_name |  str |  | The name of the class. |
| doc |  str |  | The text of the unsorted document. |

_Returns:_  The text of the sorted document.
# VarDoc

`from py_md_doc.var_doc import VarDoc`

Create a table of variables from a Python script. The variables are assumed to be commented like:

```
# This is the comment.
VAR: int = 0
```

...and the output will be this:

| Variable | Type | Value | Description |
| --- | --- | --- | --- |
| `VAR` | int | 0 | This is the comment. |

***

#### get

**`VarDoc.get(src, dst)`**

_(Static)_


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| src |  Union[str, Path] |  | The path to the source file. Can be a string or Path object. |
| dst |  Optional[Union[str, Path] |  | The path to the destination file. If None, don't write a file. Otherwise, can be a string or Path object. |

_Returns:_  The text of the API document.


from pathlib import Path
from py_md_doc import PyMdDoc

if __name__ == "__main__":
    md = PyMdDoc(input_directory=Path("py_md_doc"),
                 files=["py_md_doc.py", "parameter.py", "var_doc.py", "class_inheritance.py"],
                 metadata_path="metadata.json")
    md.get_docs(output_directory=Path("docs"))

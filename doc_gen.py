from pathlib import Path
from py_md_doc import PyMdDoc
from py_md_doc.class_inheritance import ClassInheritance

if __name__ == "__main__":
    input_directory = Path("py_md_doc")
    output_directory = Path("docs")
    md = PyMdDoc(input_directory=input_directory,
                 files=["parameter.py", "var_doc.py"],
                 metadata_path="metadata.json")
    ci = ClassInheritance(metadata_path="metadata.json")
    import_path = "py_md_doc"
    ci.get_from_directory(input_directory=input_directory,
                          output_directory=output_directory,
                          import_prefix=f"from {import_path}",
                          import_path=import_path,
                          includes=["doc_base.py", "py_md_doc.py", "class_inheritance.py"])
    md.get_docs(output_directory=output_directory)

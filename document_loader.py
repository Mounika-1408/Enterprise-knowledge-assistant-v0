from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader
)

import os


def load_document(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        loader = PyPDFLoader(file_path)

    elif extension == ".docx":
        loader = Docx2txtLoader(file_path)

    elif extension == ".txt":
        loader = TextLoader(file_path)

    elif extension == ".csv":
        loader = CSVLoader(file_path)

    else:
        raise ValueError("Unsupported file format.")

    documents = loader.load()

    # Add metadata
    department = os.path.basename(os.path.dirname(file_path))
    file_name = os.path.basename(file_path)

    for doc in documents:
        doc.metadata["department"] = department
        doc.metadata["file_name"] = file_name
        doc.metadata["file_type"] = extension

    return documents
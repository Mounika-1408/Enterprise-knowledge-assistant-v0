from document_loader import load_document
from vector_store import create_vector_store
from llm import load_llm
from prompt import load_prompt

import os

llm = load_llm()
prompt = load_prompt()


def initialize_assistant(knowledge_base):

    all_documents = []

    for root, _, files in os.walk(knowledge_base):

        for file in files:

            file_path = os.path.join(root, file)

            try:
                docs = load_document(file_path)
                all_documents.extend(docs)

            except ValueError:
                continue
        retriever = create_vector_store(
    all_documents,
    knowledge_base
)

    return retriever


def ask_question(retriever, question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    sources = []

    for doc in docs:

        department = doc.metadata.get(
            "department",
            "Unknown"
        )

        file_name = doc.metadata.get(
            "file_name",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "Unknown"
        )

        if page != "Unknown":
            page += 1

        sources.append(
            f"Department: {department} | Document: {file_name} | Page: {page}"
        )

    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(final_prompt)

    return response.content, list(set(sources))
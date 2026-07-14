import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def create_vector_store(documents, knowledge_base):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create a unique database folder for each knowledge base
    db_name = os.path.basename(os.path.normpath(knowledge_base))

    persist_directory = os.path.join(
        "chroma_db",
        db_name
    )

    # Load existing vector database
    if os.path.exists(persist_directory):

        print(f"\nLoading knowledge base '{db_name}'...\n")

        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )

    # Create new vector database
    else:

        print(f"\nCreating knowledge base '{db_name}'...\n")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(documents)

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=persist_directory
        )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    return retriever
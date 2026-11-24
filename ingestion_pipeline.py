import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma 
from dotenv import load_dotenv

load_dotenv()

def load_documents(docs_path="docs"):
    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"Documents directory not found: {docs_path}")

    loader = DirectoryLoader(docs_path, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()

    if len(documents) == 0:
        raise ValueError("No documents found in the specified directory")


    print(f"Loaded {len(documents)} documents from {docs_path}")

    for i,doc in enumerate(documents):
        print(f"Document {i+1}/{len(documents)}: {doc.metadata}")
        print(f"Content preview: {doc.page_content[:100]}...")


    return documents


# def split_documents(documents, chunk_size=1000, chunk_overlap=200):
#     text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
#     chunks = text_splitter.split_documents(documents)
#     print(f"Split documents into {len(chunks)} chunks")
#     return chunks


# def embed_chunks(chunks):
#     embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
#     chunk_embeddings = embeddings.embed_documents([chunk.page_content for chunk in chunks])
#     print(f"Embedded {len(chunk_embeddings)} chunks")
#     return chunk_embeddings


def main():
    print("Starting ingestion pipeline...")

    #1. Load Documents
    documents = load_documents()


    

if __name__=="__main__":
    main()
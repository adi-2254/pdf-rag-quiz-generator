from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()


#Load the pdf into our python program
pdf_path = Path(__file__).parent/"climates.pdf"
docs = PyPDFLoader(file_path=pdf_path).load()

#print(docs[0]) loading is done via page basis

#Chunking process via recursive chunking 
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = text_splitter.split_documents(documents=docs)


#vector embeddings

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
)


vector_store = QdrantVectorStore.from_documents(
    documents = chunks,
    embedding = embedding_model,
    url = "http://localhost:6334",
    collection_name = "quiz_taker"
)

print("Indexing of documents done...")
import os
import pinecone
import tiktoken
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

api_key = os.environ["PINECONE_API_KEY"]

env = "gcp-starter"
index_name = "knowledge-base-eliminatorias"
dimension = 1536

pinecone.init(api_key = api_key, environment = env)

if index_name not in pinecone.list_indexes():

    pinecone.create_index(
        index_name, 
        dimension = dimension
    )

    print("Index " + index_name + " creado con éxito en Pinecone")

from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter

loader = WebBaseLoader(
    [
    "https://www.marca.com/co/2023/10/17/652e070f22601d73648b4585.html", 
    "https://hiraoka.com.pe/blog/post/eliminatorias-sudamericanas-mundial-2026-calendario-partidos-y-fechas"
    ]
)

data = loader.load()

#Genera varios fragmentos de 400 tokens
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size = 400, 
    chunk_overlap = 20
)

docs = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings()
docsearch = Pinecone.from_documents(docs, embeddings, index_name = index_name)

print("Se guardaron en total " + str(len(docs)) + " embedings en Pinecone (index : " + index_name + ")")
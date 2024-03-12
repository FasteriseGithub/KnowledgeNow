


from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

def load_file(data):
    loader = DirectoryLoader("data",
                    glob="**/*.txt",
                    loader_cls= TextLoader)
    text_documents = loader.load()
    return text_documents
     

#split documents into chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    documents = text_splitter.split_documents(extracted_data)

    return documents

#creating an embedding
def data_embedding():
    embeddings = OpenAIEmbeddings()
    return embeddings
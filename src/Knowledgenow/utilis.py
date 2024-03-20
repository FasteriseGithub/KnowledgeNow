from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.messages.human import HumanMessage
from langchain.memory import ConversationBufferWindowMemory
from langchain.tools import tool
import os

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




def memory2str(memory:ConversationBufferWindowMemory):
    messages = memory.chat_memory.messages
    memory_list = [
        f"Human: {mem.content}" for mem in messages 
    ]
    memory_str = "/n".join(memory_list)
    return memory_str


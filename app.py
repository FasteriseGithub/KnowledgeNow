#import Lbraries
import streamlit as st 
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain_community.embeddings import OpenAIEmbeddings
import pinecone
from langchain.llms import OpenAI
from langchain_community.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os
from langchain.memory import ConversationBufferWindowMemory
from langchain.tools.retriever import create_retriever_tool
from langchain_pinecone import PineconeVectorStore
import pickle 
import os
from dotenv import load_dotenv 
import chardet


load_dotenv()

#add your api_keys
openai_api_key = os.getenv("OPENAI_API_KEY")
os.getenv("PINECONE_API_KEY")



#Sidebar contents
with st.sidebar:
    st.title("Fastrise Chat App")
    st.markdown('''
                ## About 
                This app is an LLM-powered chatbot built using:
                
                -[Fastrise Knowledge base](fasterise.com)
                
                -[Langchain](https://python.langchain.com)
                
                -[OpenAI](https://platform.openai.com/docs/models)
                ''')
    st.write("Made with love by KUBA")


def main():
    st.header("KNOWLEDGENOW")

    #upload a PDF file 
    text_file = st.file_uploader("upload your file", type=["txt"])
    raw_data = text_file.read(10000)  # Read the first 10000 bytes to guess encoding
    encoding = chardet.detect(raw_data)['encoding']
    #st.write(text_file.name)
    
    if text_file is not None:
        # Ensure the file pointer is at the start
        text_file.seek(0)

        # Read the file line by line into a list
        file_lines = [line.decode(encoding).strip() for line in text_file]

         
   # Load the text document using TextLoader
    text_reader = UnstructuredFileLoader(file_lines)
    text_document = text_reader.load()
    



    st.write(text_document)

    
    


if __name__ =="__main__":
    main()

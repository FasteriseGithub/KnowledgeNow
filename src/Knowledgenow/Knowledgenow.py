#import standard libraries
import os
from typing import List
import json
import logging 

#import Langchain Lbraries
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain.memory import ConversationBufferWindowMemory
from langchain.tools.retriever import create_retriever_tool
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_experimental.text_splitter import SemanticChunker
from langchain.tools import tool
from langchain.agents import create_react_agent
from langsmith import Client
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain. retrievers.multi_query import MultiQueryRetriever
from langchain_core.messages.human import HumanMessage
from langchain.memory import ConversationBufferMemory
from src.Knowledgenow.logger import logging

#import pinecone libraries
import pinecone
from langchain_pinecone import PineconeVectorStore

#import secret keys
from dotenv import load_dotenv 
load_dotenv()

#Accessing the secret keys
openai_api_key = os.getenv("OPENAI_API_KEY")
pine_cone_api = os.getenv("PINECONE_API_KEY")

#setup Langsmith for debugging
from uuid import uuid4

unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {unique_id}"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "ls__c4c7a9772ef046038636017b03b5f17b"

#loading the prompt templates
from importlib import reload
import prompts.prompts_2024_03_26 as prompts
reload(prompts)

#initiaze language models
llm  = ChatOpenAI(
    openai_api_key=openai_api_key, 
    model="gpt-4-turbo-preview", 
    temperature= 0.0
    )

#import global context file 
with open("Fastrise_global_context.txt", "r") as file:
    global_context = file.read()
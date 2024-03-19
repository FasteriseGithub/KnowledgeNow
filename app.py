#import Lbraries
import streamlit as st 
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain_community.embeddings import OpenAIEmbeddings
import pinecone
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate, ChatPromptTemplate
import os
from langchain.memory import ConversationBufferWindowMemory
from langchain.tools.retriever import create_retriever_tool
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv 
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParserOutputParser
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
load_dotenv()

#add your api_keys
openai_api_key = os.getenv("OPENAI_API_KEY")
os.getenv("PINECONE_API_KEY")



if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

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




#get  response 
def get_response(query, chat_history):
    template = """
 Your role is to use the global context to answer any question from users. 


 {chat_history}

 global_context: {global_context}

Begin!

 Question: {input}

 Thoughts: {agent_scratchpad}
 
 """


prompt = ChatPromptTemplate.from_template(template=template, MessagePlaceholder=["(agent_scratchpad)"])



llm  = ChatOpenAI(
    openai_api_key=openai_api_key, 
    model="gpt-4-turbo-preview", 
    temperature= 0.0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]

    )



#conversations
for message in st.session.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    

    else:
        with st.chat_message("AI"):
            st.markdown(message.content)

#user input
user_query = st.chat_input("Your message")
if user_query is not None and user_query !="":
    st.session_state.chat_history.append(HumanMessage(user_query))


    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        ai_response = "i don't know"
        st.markdown(ai_response)
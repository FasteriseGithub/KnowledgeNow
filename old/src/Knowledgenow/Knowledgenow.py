#import Lbraries
import pinecone
from dotenv import load_dotenv 
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
import os
from langchain_core.messages import SystemMessage
from langchain.memory import ConversationBufferWindowMemory
from langchain.tools.retriever import create_retriever_tool
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_experimental.text_splitter import SemanticChunker
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_pinecone import PineconeVectorStore
from langchain. retrievers.multi_query import MultiQueryRetriever
from langchain.tools import tool
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain_core.messages.human import HumanMessage
from src.Knowledgenow.utilis import load_file, text_split, data_embedding, memory2str
from src.Knowledgenow.logger import logging

#load environment variables from the .env file

load_dotenv()


openai_api_key = os.getenv("OPENAI_API_KEY")

pinecone_api_key = os.getenv("PINECONE_API_KEY")

YOUR_API_KEY = os.getenv("PINECONE_API_KEY")



#extract the data 
extracted_data = load_file([ "2024-03-12_Dev_Meeting_-_Knowledge_Now_summary_1.txt", "2024-03-12-Dev-Meeting-Knowledge-Now-Transcrpt-2.txt"])

#split documents into chunks
text_chunk = text_split(extracted_data)

#creating embeddings
embeddings = data_embedding()

#inserting the embeddings into a vectorstore

Your_env = "gcp-starter"

index_name = "knowledgenow"

vectorstore = PineconeVectorStore.from_documents(text_chunk, embeddings, index_name=index_name)

#initializing retrival
retriver = vectorstore.as_retriever(search_kwargs={'k':25})

#initiaze language models
llm  = ChatOpenAI(
    openai_api_key=openai_api_key, 
    model="gpt-4-turbo-preview", 
    temperature= 0.0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]

    )

retriever = MultiQueryRetriever.from_llm(
    retriever=retriver, llm=llm
)

logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)


#retrival chain
qa = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=retriever
)

#creating a custom tool
@tool
def Knowledgebase(query:str)-> str:
    """
    Use this tool when answering question about meeting, task, activities in a organization called Fastrise"""
    result_str = qa.invoke(query)
    return result_str

global_context = """Fasterise

### Mission and Vision
- *Mission and Vision*: Fasterise is centered around leveraging AI technology to amplify human potential, prioritizing ethical AI development that enriches human capabilities. The company envisions a future where AI solutions address societal needs and business challenges while augmenting the human potential and keeping it at the center of the system.
### Team Structure and Roles
- *Henry*: Brings AI and entrepreneurial insights, contributing significantly to the team's innovative capabilities in AI and LangChain.
- *Zach*: Offers sales expertise and a keen sense for impactful business development, essential for guiding the company's market direction.
- *Paige*: With a background in education and a focus on ethical AI, Paige drives the mission, marketing vision, and operational strategies of the company.
- *Pawel*: Provides business analysis and client-facing skills, ensuring professional and confident representation of Fasterise's image.
- *Bartek*: Leads in engineering with expertise in Prompt Engineering and AI Agents, and a focus on system design and test-driven development, enhancing the company's technical rigor.
- *Alejo*: Plays a key role in Operations, Sales, and Development. In development, Alejo focuses on developer guidance through Scrums, making the vision of the company more tangible into projects with a particular emphasis on AI technologies like RAG, LLMs and Multi-Agent Systems.
- *Hubi*: is diving into Python, LangChain and RAG. He has experience in front end development.
- *Jorg*: Contributes to social media content and marketing campaigns, showcasing the company's solutions through various platforms.
- *Kuba*: has played a key role in LangChain and RAG efforts, creating the first versions of the Pinecone Vector Database chat and the Personalized Outreach System.
### Projects and Operations
- *Completed Projects*: Highlight projects like the Ski Chalet Concierge, Scheduler Assistant, and Lead Qualifier, which exemplify Fasterise's commitment to enhancing operational efficiency and customer experience through AI.
- *Current Projects*: Emphasize the development of innovative solutions like the Zoom Transcriber to Pinecone Integration, Knowledge Base Builder called KnowledgeNow, Personalized Outreach System, Administrative Automation Tools, and Real Estate-focused AI Solutions. These projects aim to integrate AI across various industries, improving efficiency and amplifying human capabilities.
- *Future Direction*: Focus on continuous exploration of AI applications, with a commitment to adapting to technological advancements and exploring areas where AI can have a transformative societal impact, keeping empowerement and education at the forefront of the company's mission.
### Company Culture and Values
- *Profit-Sharing and Collaboration*: All team members are co-founders, with a profit-sharing structure and collective decision-making. The company culture promotes innovation, ethical business practices, and a shared vision for the impact of AI technology.
- *Ethical and Human-Centered Approach*: A foundational commitment to developing AI solutions that align with ethical standards, enhance rather than replace human work, and focus on amplifying human capabilities.
### Innovations and Products
- *Technological Innovations*: AI-driven products, including AI solutions for real estate, personalized outreach, and KnowledgeNow. High technological sophistication and human-centered design of products like automated CRM and calendar systems, which facilitate better interactions with leads and clients.
### Conclusion
Fasterise stands out for its innovative approach to AI technology, with a strong emphasis on ethical development, collaborative innovation, and a culture of shared success. Through a diverse range of projects, the company showcases its capability to address complex challenges across various sectors, aiming for a significant societal impact and leading by example in the ethical use and development of AI.
"""

#creating a prompt template

template = """
 Your role is to use the global context to answer any question from users. 


 {chat_history}

 global_context: {global_context}

Begin!

 Question: {input}

 Thoughts: {agent_scratchpad}
 
 """

prompt = PromptTemplate.from_template(template=template, MessagePlaceholder=["(agent_scratchpad)"])

tools = [Knowledgebase]

agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query ="what project was bartek and Alejo discuss in the meeting"

out = agent_executor.invoke({"input": query,
                       "chat_history": [],
                       "global_context":global_context })

#conversational memory 
conversational_memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k=5,
    return_messages=True

)

conversational_memory.chat_memory.add_user_message(query)
conversational_memory.chat_memory.add_ai_message(out["output"])


memory2str(conversational_memory)


def chat(text:str):
    out = agent_executor.invoke({
        "input":text, 
        "chat_history": [memory2str(conversational_memory)], 
        "global_context": global_context})
    conversational_memory.chat_memory.add_user_message(text)
    conversational_memory.chat_memory.add_ai_message(out["output"])
    return out["output"]



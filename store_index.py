from src.helper import load_file, text_split, data_embedding 
from langchain.vectorstores import pinecone
import pinecone 
from dotenv import load_dotenv
import os
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import pinecone


load_dotenv()

os.environ["OPENAI_API_KEY"]= "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"

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


#print(PINECONE_API_KEY)

extracted_data = load_file("data\meeting_transcript.txt")
text_chunk = text_split(extracted_data)
embeddings = data_embedding()

#load pinecone index name
index_name = "knowledgenow"

#creating embedding for each of the text Chunks and store in the vectordatabase
vectorstore = PineconeVectorStore.from_documents(text_chunk, embeddings, index_name=index_name)

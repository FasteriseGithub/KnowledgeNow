from flask import Flask, render_template, jsonify, request
from src.helper import data_embedding
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os
from langchain_openai.chat_models import ChatOpenAI

app = Flask(__name__)

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")
pinecone_api_key = os.environ.get("PINECONE_API_KEY")

embeddings = data_embedding()
index_name = "knowledgenow"
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

prompt = PromptTemplate(template=template, input_variables=["context", "question"])

chain_type_kwargs = {"prompt": prompt}

llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo")

retriever = vectorstore.as_retriever(search_kwargs={'k': 2})

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs=chain_type_kwargs
)

@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=['GET',"POST"])
def chat():
    msg = request.form["msg"]
    input = msg 
    print(input)
    result=qa({"query": input})
    print("Response:", result["result"])
    return str(result["result"])

if __name__ == "__main__":
    app.run(debug=True)

# RAG Chatbot Based on Fastrise Zoom Meeting Transcript

This project implements a RAG (Retrieval-augmented generation) chatbot based on Fastrise Zoom meeting transcripts. The RAG chatbot is a management tool used to quickly confirm tasks and to do verify information.

### File Structure (unfinished)

project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── datasets.py
├── domain/
│   ├── models.py
│   └── services.py
├── application/
│   ├── use_cases/
│   └── controllers.py
├── infrastructure/
│   ├── data_sources.py
│   └── repositories.py
├── tests/
│   ├── test_models.py
│   └── test_services.py
├── docs/
│   └── README.md
├── requirements.txt
└── main.py


## Setup

Follow these steps to set up and run the project:

### Step 1: Create a Virtual Environment

```
bash
 
 python -m venv env

```

```
bash
.\env\Scripts\activate
```
### Step 2: Install Dependencies

```
bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

```
bash
# Pinecone API Key
PINECONE_API_KEY = "your_pinecone_api_key_here"
# OpenAI API Key
OPENAI_API_KEY = "your_openai_api_key_here"
'''


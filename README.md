# KnowledgeNow

This project implements a multi-agent RAG system based on Fasterise's Zoom meeting transcripts. 
The initial MVP is a task management tool for devs to keep track of their deliverables, confirm details of each deliverable and understand the objective of the deliverable in the larger scope of the whole project.

### File Structure for MVP

```
KnowledgeNow/
├── data/
│   ├── raw/
│   ├── data_processing_pipeline.py
│   ├── processed/
│   │   ├── transcripts/
│   │   ├── discord_chats.txt
│   │   └── global_context.txt
├── prompts/
│   ├── current/
│   └── archived/
├── utils/
│   ├── airtable.py
│   ├── pinecone/
│   │   ├── upload_doc.py
│   │   ├── retrieve.py
├── infrastructure/
│   ├── discord.py
│   ├── streamlit.py
│   └── docker/
├── tests/
│   ├── standard_tests.py
│   └── use_case_tests.py
├── logs/
│   ├── logs.txt
│   ├── langsmith.py
│   └── outputs.py
├── scripts/
├── config/
│   ├── config.json
│   └── streamlit.json
├── documentation/
│   ├── user_guide.md
│   ├── diagrams.md
├── README.md
├── requirements.txt
└── main.py
```



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


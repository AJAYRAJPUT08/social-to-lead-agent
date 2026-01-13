# Social-to-Lead Agentic Workflow 🤖🚀

This project demonstrates a **GenAI-powered conversational agent** that converts user conversations into **qualified sales leads**.  
It showcases a complete **agentic workflow** using **intent detection, RAG (Retrieval-Augmented Generation), and tool execution**.

This project was built as part of a **Machine Learning / GenAI Internship assignment**.

---

## 🧠 Problem Statement

Businesses receive many messages on social platforms, but only a small percentage of users are genuinely interested in buying.  
Manually identifying such users and collecting their details is inefficient.

### Goal
Build an AI agent that:
- Answers product-related questions
- Detects high-intent users
- Captures lead details automatically

---

## 🧩 Solution Overview

The system works as a **Social-to-Lead Agent**:

1. User interacts with the chatbot
2. The agent detects the user's intent
3. Product queries are answered using RAG
4. High-intent users are asked for contact details
5. Lead data is saved using a tool

---

## 🏗️ Architecture (Agentic Workflow)



## ⚙️ Installation & Setup

### 1️⃣ Python Version
Make sure **Python 3.11** is installed.

### 2️⃣ Install Required Libraries
```bash
pip install langchain langchain-community langchain-text-splitters langchain-groq faiss-cpu python-dotenv pydantic





User
↓
Intent Detection (LLM)
↓
Agent Decision Logic
├─ Product / Pricing / Feature → RAG Response
└─ High Intent → Lead Capture Tool
↓
Lead Stored (CSV)


---

## 🛠️ Tech Stack

- **Python 3.11**
- **Groq LLM** (llama-3.1-8b-instant)
- **LangChain**
- **FAISS** (vector similarity search)
- **Manual RAG implementation**
- **CSV-based tool execution**

---

## 📂 Project Structure




social-to-lead-agent/
│
├── app.py # Main chatbot loop
├── agent.py # Agent decision logic
├── intent.py # Intent detection using LLM
├── rag.py # RAG (FAISS + LLM)
├── tools.py # Lead capture tool
├── knowledge_base.txt # Product knowledge
├── leads.csv # Stored leads
├── .env # GROQ API key (not pushed to GitHub)
└── README.md



Thank You !

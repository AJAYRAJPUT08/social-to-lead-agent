from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Load knowledge
loader = TextLoader("knowledge_base.txt")
documents = loader.load()

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# Fake embeddings (no API key needed)
embeddings = FakeEmbeddings(size=768)
vectorstore = FAISS.from_documents(docs, embeddings)

# Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def rag_answer(question: str) -> str:
    relevant_docs = vectorstore.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in relevant_docs])

    prompt = f"""
You are a SaaS assistant.
Answer ONLY using the context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content

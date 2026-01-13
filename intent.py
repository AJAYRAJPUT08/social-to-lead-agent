from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def detect_intent(user_message: str) -> str:
    prompt = f"""
Classify the intent of the message into one of these:
product_query
pricing_query
feature_query
high_intent_lead
casual

Message:
{user_message}

Respond with ONLY the intent name.
"""

    response = llm.invoke(prompt)
    return response.content.strip()

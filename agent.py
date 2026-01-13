from intent import detect_intent
from rag import rag_answer

def run_agent(user_message: str):
    intent = detect_intent(user_message)

    if intent in ["product_query", "pricing_query", "feature_query"]:
        answer = rag_answer(user_message)
        return answer, False

    elif intent == "high_intent_lead":
        return "🔥 You seem interested! Can I get your name and email?", True

    else:
        return "🙂 How can I help you learn more about LeadFlow AI?", False

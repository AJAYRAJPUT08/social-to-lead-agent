from agent import run_agent
from tools import capture_lead
import re

print("🤖 LeadFlow AI Assistant")
print("Type 'exit' to quit\n")

waiting_for_lead = False
lead_interest = ""

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    if waiting_for_lead:
        email_match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            user_input
        )

        if email_match:
            email = email_match.group()
            name = user_input.replace(email, "").replace(",", "").strip()

            if not name:
                name = "Unknown"

            result = capture_lead(name, email, lead_interest)
            print("Bot:", result)
            waiting_for_lead = False
        else:
            print("Bot: Please share your email (example: ajay@gmail.com)")
        continue

    response, needs_lead = run_agent(user_input)
    print("Bot:", response)

    if needs_lead:
        waiting_for_lead = True
        lead_interest = user_input

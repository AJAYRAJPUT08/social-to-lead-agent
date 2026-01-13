import csv
from datetime import datetime

def capture_lead(name: str, email: str, interest: str):
    """
    Save lead information into leads.csv
    """

    with open("leads.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header only if file is empty
        if file.tell() == 0:
            writer.writerow(["name", "email", "interest", "timestamp"])

        writer.writerow([
            name,
            email,
            interest,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])

    return "✅ Lead captured successfully!"

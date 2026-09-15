from ai_service import generate_answer


context = """
The shipment system reads product information from CSV files.
It combines shipment products with shipment locations and
inserts the information into a database.
"""

question = "What does the shipment system read?"

answer = generate_answer(question, context)

print("\nAI Answer:\n")
print(answer)
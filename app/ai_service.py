import ollama


def generate_answer(question, context):

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

If the answer is not in the context, say:
"I could not find the answer in the document."
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
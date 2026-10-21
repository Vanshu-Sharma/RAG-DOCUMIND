from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(
    question,
    context,
    history=""
):

    prompt = f"""
You are DocuMind AI.

Use the conversation history and document context
to answer the question.

Conversation History:
{history}

Document Context:
{context}

Question:
{question}

Answer:
"""\

    response = client.chat.completions.create(
        model="qwen/qwen3.8-27b",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
        max_completion_tokens=800
        ]
    )

    return response.choices[0].message.content

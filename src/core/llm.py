
from groq import Groq, RateLimitError
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question, context, history=""):
    prompt = f"""
You are DocuMind AI, a document question-answering assistant.

Instructions:
- Answer using the supplied document context and relevant conversation history.
- Be concise and directly answer the question.
- Do not invent facts or claim the document says something it does not.
- If the context is insufficient, clearly state that.
- For requests asking for all headings or subheadings, list only those
  explicitly supported by the supplied context.

Conversation History:
{history}

Document Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=512,
            temperature=0.2,
        )

        return response.choices[0].message.content or (
            "The model returned an empty response."
        )

    except RateLimitError:
        return (
            "The model's output-token rate limit has been reached. "
            "Please wait for the limit to reset, then try again. "
            "If this happens frequently, check your Groq usage limits."
        )

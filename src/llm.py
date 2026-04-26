import requests

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a precise assistant.

You are a precise assistant for answering questions based ONLY on the given context.

Rules:
- Use only the context below
- If answer is not in context, say "Not found in the document"
- Be concise and factual
- Be Very Thankful


Context:
{context}

Question:
{query}

Answer briefly:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
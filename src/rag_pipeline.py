from src.retriever import retrieve_chunks
from src.llm import ask_llm


def answer_question(question):
    """
    Complete Retrieval-Augmented Generation pipeline.
    """

    results = retrieve_chunks(question)

    retrieved_chunks = results["documents"][0]

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are an engineering assistant.
Answer ONLY using the engineering reference material below.
Engineering Reference
---------------------
{context}

Question:
{question}

Answer:
"""

    return ask_llm(prompt)
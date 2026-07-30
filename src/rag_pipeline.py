from src.retriever import retrieve_chunks
from src.llm import ask_llm


def answer_question(question, chat_history=None):
    results = retrieve_chunks(question)

    documents = results["documents"][0]
    sources = results["metadatas"][0]
    distances = results["distances"][0]

    if not distances:
        return (
            "No indexed engineering documents were found. Please upload and index documents first.",
            [],
            []
        )

    best_distance = min(distances)

    if best_distance > 1.45:
        return (
            "I couldn't find relevant information about that in the uploaded engineering documents.",
            [],
            []
        )

    context = ""

    filtered_sources = []
    filtered_distances = []

    for doc, source, distance in zip(documents, sources, distances):

        # Keep only chunks that are close to the best match
        if distance <= best_distance + 0.05:

            context += (
                f"Source: {source['source']}\n"
                f"{doc}\n\n"
            )

            filtered_sources.append(source)
            filtered_distances.append(distance)

    history = ""

    if chat_history:

        recent_history = chat_history[-6:]  # last 3 user/assistant exchanges

        history = ""

        for message in recent_history:
            history += (
                f"{message['role'].capitalize()}: "
                f"{message['content']}\n"
            )

    prompt = f"""
        You are an expert mechanical engineering assistant.

        Use the engineering reference material below as your primary source.

        If the reference material contains closely related engineering concepts,
        you may explain them and make standard engineering connections.

        Do not invent facts or use unrelated outside knowledge.

        If the reference material is unrelated to the user's question,
        say that you could not find enough relevant information.

        Conversation History
        --------------------
        {history}

        Engineering Reference
        ---------------------
        {context}

        Current Question
        ----------------
        {question}
    """

    answer = ask_llm(prompt)

    return answer, filtered_sources, filtered_distances
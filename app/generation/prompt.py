def build_prompt(query, contexts):
    formatted_context = ""

    for c in contexts:
        clause_id = c["metadata"].get("clause", "Unknown")
        formatted_context += f"[Source: {clause_id}]\n{c['text']}\n\n"

    return f"""
You are a legal research assistant.

Answer the question using ONLY the sources provided below.
Do NOT add any information that is not present in the sources.

Your response MUST have two sections:
1. Answer
2. Sources (list clause identifiers)

If the answer is not present, respond exactly with:
"Insufficient data found in internal documents."

Sources:
{formatted_context}

Question:
{query}

Answer:
"""

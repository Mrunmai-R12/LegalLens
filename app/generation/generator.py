from transformers import pipeline
from app.generation.prompt import build_prompt

# Load model once
_generator = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base",
    max_length=512
)

def generate(query, contexts):
    if not contexts:
        return "Insufficient data found in internal documents."

    prompt = build_prompt(query, contexts)

    result = _generator(
        prompt,
        do_sample=False
    )[0]["generated_text"].strip()

    # Safety check: enforce source presence
    if "Source" not in result and "Sources" not in result:
        return "Insufficient data found in internal documents."

    return result

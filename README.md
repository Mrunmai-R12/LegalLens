# LegalLens – AI-Powered Legal Research Assistant

LegalLens is a prototype implementation of a Retrieval-Augmented Generation (RAG)
system designed for legal document search and question answering.

The system enables attorneys to query internal legal documents using natural language
and receive grounded, citation-backed answers.

---

## System Architecture

LegalLens follows a retrieval-first RAG architecture:

1. Legal documents are split into clause-level chunks
2. Clauses are embedded using a legal-domain model
3. Relevant clauses are retrieved via semantic search
4. An instruction-tuned LLM generates a grounded answer

---

## Model Choices and Rationale

### Retrieval (Semantic Search)
- **Model:** `nlpaueb/legal-bert-base-uncased`
- **Reason:** Optimized for legal language understanding and clause-level semantic similarity

### Generation (Answer Synthesis)
- **Model:** `google/flan-t5-base`
- **Reason:** Instruction-tuned, CPU-friendly, and suitable for grounded text generation

Encoder-only models such as Legal-BERT are used exclusively for retrieval, while
generation is handled by an encoder-decoder model.

---

## Key Features
- Clause-level, context-aware document chunking
- Legal-domain semantic retrieval using FAISS
- Grounded answer generation with refusal on insufficient context
- FastAPI-based service architecture
- No external API dependencies or billing requirements

---

## Running the Project Locally
```bash
1. Install dependencies:
pip install -r requirements.txt

2.Start the server:
uvicorn app.main:app --reload

3.Query the system:
POST http://localhost:8000/query
{
  "question": "Is there a provision for termination without cause?" 
}

Disclaimer

This project is a proof-of-concept created for casestudy evaluation.
It focuses on system design, retrieval quality, and safety rather than
production-scale deployment.
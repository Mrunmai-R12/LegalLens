from fastapi import APIRouter
from app.models.schemas import QueryRequest, QueryResponse
from app.retrieval.retriever import retrieve
from app.generation.generator import generate

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_docs(req: QueryRequest):
    contexts = retrieve(req.question)
    answer = generate(req.question, contexts)
    return QueryResponse(answer=answer)

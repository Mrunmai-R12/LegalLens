from fastapi import FastAPI
from app.api import router
from app.startup import load_documents

app = FastAPI(title="LegalLens API")

@app.on_event("startup")
def startup():
    load_documents()

app.include_router(router)

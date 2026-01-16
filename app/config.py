from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    EMBEDDING_MODEL: str = "nlpaueb/legal-bert-base-uncased"
    TOP_K: int = 5

    class Config:
        env_file = ".env"

settings = Settings()

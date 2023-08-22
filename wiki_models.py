from pydantic import BaseModel


class Article(BaseModel):
    result: str | None = None
    articles: list[str] | None = None

from fastapi import FastAPI

from src.http.wiki_api import router as wiki_router


app = FastAPI()
app.include_router(wiki_router)
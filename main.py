from fastapi import FastAPI

from wiki_api import router as wiki_router


app = FastAPI()
app.include_router(wiki_router)
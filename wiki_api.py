from typing import Annotated
from aiohttp import ClientSession
from fastapi import Header, APIRouter
from fastapi.responses import JSONResponse

from wiki_models import WikiInfo
from repository import Repository
from wiki_request import WikiRequest


router = APIRouter(tags=["WIKI"])


@router.get(
    "/wiki/{request}",
    responses={
        200: {"model": WikiInfo, "description": "Ok"},
        303: {"model": WikiInfo, "description": "See Other"},
        404: {"model": WikiInfo, "description": "Not found any articles"},
    },
    summary="Get articles",
)
async def wiki_info(
    request: str,
    Accept_Language: Annotated[str, Header()],
) -> JSONResponse:
    
    async with ClientSession() as sess:
        wr = WikiRequest(session=sess)
        repo = Repository(wiki_request=wr)
        result = await repo.get_wiki_info(request=request, language=Accept_Language)

        if all([result.first_article_paragraph != None, result.article_titles]):
            return JSONResponse(content=result.model_dump(), status_code=200)
        elif all([result.first_article_paragraph == None, result.article_titles]):
            print(result)
            return JSONResponse(content=result.model_dump(), status_code=303)
        else:
            return JSONResponse(content=result.model_dump(), status_code=404)

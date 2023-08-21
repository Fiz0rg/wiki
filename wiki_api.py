from typing import Annotated
from aiohttp import ClientSession
from fastapi import Header, APIRouter

from wiki_repository import WikiRepository


router = APIRouter(tags=["WIKI"])


@router.get('/wiki/{request}',
            responses={
                200: {'model': dict, 'description': 'Ok'},
                303: {'model': dict, 'description': 'See Other'},
                404: {'model': dict, 'description': 'Not found any articles'},
            },
            summary="Get articles",
)
async def wiki_info(
    request: str,
    Accept_Language: Annotated[str, Header()],
):
    async with ClientSession() as sess:

        repo = WikiRepository(session=sess)
        result = repo.get_wiki_info(request=request, language=Accept_Language)
        return await result

from typing import Annotated

from src.data.repository.wiki import WikiRepository

from fastapi import Header, APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(tags=["WIKI"])


@router.get('/wiki/{request}',
            responses={
                200: {'model': dict, 'description': 'Ok'},
                303: {'model': dict, 'description': 'See Other'},
                404: {'model': dict, 'description': 'Not found any articles'},
            })
async def run(
    request: str,
    language: Annotated[str| None, Header()] = None
) -> JSONResponse:
    
    result = WikiRepository.get_article(
        request=request,
        language=language,
    )

    return await result
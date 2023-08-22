from aiohttp import ClientSession
import pytest

from fastapi.responses import JSONResponse

from repository import Repository
from wiki_models import Article
from wiki_request import WikiRequest

from tests.fixtures.const import DEFAULT_TEST_USECASE_TASK_ID


@pytest.mark.asyncio
async def test_full():
    async with ClientSession() as sess:
        wr = WikiRequest(session=sess)
        repo = Repository(wiki_request=wr)

        result = await repo.get_wiki_info(
            request='rum',
            language=DEFAULT_TEST_USECASE_TASK_ID
        )
    assert isinstance(result, JSONResponse)
    assert JSONResponse(content=Article, status_code=200) 


@pytest.mark.asyncio
async def test_half():
    async with ClientSession() as sess:
        wr = WikiRequest(session=sess)
        repo = Repository(wiki_request=wr)

        result = await repo.get_wiki_info(
            request='rumbellion',
            language=DEFAULT_TEST_USECASE_TASK_ID
        )
    assert JSONResponse(content=Article, status_code=303) 
    assert isinstance(result, JSONResponse) 


@pytest.mark.asyncio
async def test_error():
    async with ClientSession() as sess:
        wr = WikiRequest(session=sess)
        repo = Repository(wiki_request=wr)
        result = await repo.get_wiki_info(
            request='asdasdasdwadsadas',
            language=DEFAULT_TEST_USECASE_TASK_ID
        )
    assert JSONResponse(content=Article, status_code=404)
    assert isinstance(result, JSONResponse) 
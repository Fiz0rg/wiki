from aiohttp import ClientSession
import pytest

from fastapi.responses import JSONResponse

from wiki_repository import WikiRepository
from tests.fixtures.const import DEFAULT_TEST_USECASE_TASK_ID


@pytest.mark.asyncio
async def test_full():
    async with ClientSession() as sess:
        repo = WikiRepository(session=sess)
        result = await repo.get_wiki_info(
            request='rum',
            language=DEFAULT_TEST_USECASE_TASK_ID
        )
    assert result.status_code == 200
    assert isinstance(result, JSONResponse) 


@pytest.mark.asyncio
async def test_half():
    async with ClientSession() as sess:
        repo = WikiRepository(session=sess)
        result = await repo.get_wiki_info(
            request='rumbellion',
            language=DEFAULT_TEST_USECASE_TASK_ID
        )
    assert result.status_code == 303
    assert isinstance(result, JSONResponse) 


@pytest.mark.asyncio
async def test_error():
    async with ClientSession() as sess:
        repo = WikiRepository(session=sess)
        result = await repo.get_wiki_info(
            request='asdasdasdwadsadas',
            language=DEFAULT_TEST_USECASE_TASK_ID
        )
    assert result.status_code == 404
    assert isinstance(result, JSONResponse) 
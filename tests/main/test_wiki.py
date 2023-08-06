import pytest

from fastapi.responses import JSONResponse

from src.data.repository.wiki import WikiRepository
from tests.fixtures.const import DEFAULT_TEST_USECASE_TASK_ID


@pytest.mark.asyncio
async def test_full():
    result = await WikiRepository.get_article(
        request='rum',
        language=DEFAULT_TEST_USECASE_TASK_ID,
    )
    assert result.status_code == 200
    assert isinstance(result, JSONResponse) 


@pytest.mark.asyncio
async def test_half():
    result = await WikiRepository.get_article(
        request='rumbellion',
        language=DEFAULT_TEST_USECASE_TASK_ID,
    )
    assert result.status_code == 303
    assert isinstance(result, JSONResponse) 


@pytest.mark.asyncio
async def test_error():
    result = await WikiRepository.get_article(
        request='asdasdasdasdasd',
        language=DEFAULT_TEST_USECASE_TASK_ID,
    )
    assert result.status_code == 404
    assert isinstance(result, JSONResponse) 
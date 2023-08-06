import pytest

from fastapi.responses import JSONResponse

from src.data.repository.wiki import WikiRepository


@pytest.mark.asyncio
async def test_full():
    result = await WikiRepository.get_article(
        request='rum',
        language='cs'
    )
    assert result.status_code == 200
    assert isinstance(result, JSONResponse) 


@pytest.mark.asyncio
async def test_half():
    result = await WikiRepository.get_article(
        request='rumbellion',
        language='cs'
    )
    assert result.status_code == 303
    assert isinstance(result, JSONResponse) 


@pytest.mark.asyncio
async def test_error():
    result = await WikiRepository.get_article(
        request='asdasdasdasdasd',
        language='cs'
    )
    assert result.status_code == 404
    assert isinstance(result, JSONResponse) 
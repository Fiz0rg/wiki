from aiohttp import ClientSession
import pytest

from tests.const import DEFAULT_LANGUANE, FULL_RESPONSE, HALF_RESPONSE, EMPTY_RESPONSE
from repository import Repository
from wiki_models import WikiInfo
from wiki_request import WikiRequest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "req,language,response", [
        ('rum', DEFAULT_LANGUANE, FULL_RESPONSE),
        ('rumbellion', DEFAULT_LANGUANE, HALF_RESPONSE),
        ('dasdasdasdsdfs', DEFAULT_LANGUANE, EMPTY_RESPONSE)
    ]
)
async def test_eval(req, language, response):
    async with ClientSession() as sess:
        wr = WikiRequest(session=sess)
        repo = Repository(wiki_request=wr)

        result = await repo.get_wiki_info(
            request=req,
            language=language
        )
    assert result == WikiInfo(**response)

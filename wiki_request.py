from aiohttp import ClientSession

from wiki_parser import (
    get_the_first_paragraph_of_the_article,
    list_of_similar_article_titles,
)


class WikiRequest:

    def __init__(self, session: ClientSession) -> None:
        self.session = session

    async def get_article(self, *, request: str, language: str) -> str | None:
        
        """ Get a specific article. """

        search_params = {
            'action': 'query',
            'format': 'json',
            'titles': request,
            'prop': 'extracts',
            'exintro': '',
            'explaintext': '',
        }
        async with self.session.get(url=f"https://{language}.wikipedia.org/w/api.php", params=search_params) as resp:
            response = await resp.text()
            result = await get_the_first_paragraph_of_the_article(response)
            return result
        

    async def lst(self, * ,request: str, language: str) -> list[str] | None:
        """ Get a list of articles with similar titles by request. """

        search_params = {
            'list': 'search',
            'format': 'json',
            'action': 'query',
            'utf8': 1, 
            'srsearch': request, 
        }
        async with self.session.get(url=f'http://{language}.wikipedia.org/w/api.php', params=search_params) as resp:
            response = await resp.text()
            result = await list_of_similar_article_titles(response)
            return result



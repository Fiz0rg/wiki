from aiohttp import ClientSession

from wiki_request import WikiRequest
from wiki_models import Article


class Repository:

    def __init__(self, wiki_request: WikiRequest) -> None:
        self.wiki_request = wiki_request

    async def get_wiki_info(self, *, request: str, language: str) -> Article:
          
        similar_article_titles = await self.wiki_request.lst(request=request, language=language)
        particular_article = await self.wiki_request.get_article(request=request, language=language)

        if all([similar_article_titles, particular_article != None]):
            return Article(
                result=particular_article,
                articles=similar_article_titles
            )
        
        elif all([similar_article_titles, particular_article == None]):
            return Article(
                result=None,
                articles=similar_article_titles
            )
        
        else:
            return Article(
                result=None,
            )



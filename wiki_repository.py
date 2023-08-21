from aiohttp import ClientSession
from fastapi.responses import JSONResponse

from wiki_request import WikiRequest


class WikiRepository:

    def __init__(self, session: ClientSession) -> None:
        self.session = session

    async def get_wiki_info(self, *, request: str, language: str) -> JSONResponse:
        
            
        similar_article_titles = await WikiRequest.lst(session=self.session, request=request, language=language)
        particular_article = await WikiRequest.get_article(session=self.session, request=request, language=language)

        if all([similar_article_titles, particular_article['result'] != None]):
            return JSONResponse(content=particular_article | similar_article_titles, status_code=200)
        
        elif all([similar_article_titles, particular_article['result'] == None]):
            return JSONResponse(content=particular_article | similar_article_titles, status_code=303,)
        
        else:
            return JSONResponse(content={"result": None}, status_code=404)



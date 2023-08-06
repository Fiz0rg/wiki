from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse


class IWikiRepository(ABC):
    @abstractmethod
    async def get_article(self, request: str, language: str) -> JSONResponse:
        """"
        Get wiki article

        Args:
            request (str): User request to Wiki
            language (str): Required request language

        Returns: 
            JSONResponse(status_code=200): Content include the first paragraph of the article in the requested language 
                                           and articles in the requested language containing the searched term.
            JSONResponse(status_code=303): Content include articles in the requested language containing 
                                           the searched term and dict with result as None.
            JSONResponse(status_code=404): Content include dict with result as None.
                                           
        Raises:
            ArticlesDidntFind(404) 
        
        """
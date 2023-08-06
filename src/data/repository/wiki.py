from wikipedia import summary, set_lang, search

from fastapi.responses import JSONResponse

from src.core.repository.wiki import IWikiRepository


class WikiRepository(IWikiRepository):
    async def get_article(*, request: str, language: str | None = None) -> JSONResponse:

        if not language:
            set_lang("cs")

        articles = search(request)

        if articles:
            if request.title() in articles:
                result = summary(request).split("\n")[0]
                return JSONResponse(content={"result": result, "articles": articles}, status_code=200)
            else:
                return JSONResponse(content={"result": None, "articles": articles}, status_code=303)

        return JSONResponse(content={"result": None}, status_code=404)

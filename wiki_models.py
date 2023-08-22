from pydantic import BaseModel


class ArticleTitles(BaseModel):
    article_titles: list[str] | None = None


class FirstArticleParagraph(BaseModel):
    first_article_paragraph: str | None = None


class WikiInfo(ArticleTitles, FirstArticleParagraph):
    """ """

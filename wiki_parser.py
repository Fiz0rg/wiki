from json import loads


async def get_the_first_paragraph_of_the_article(row_sting: str) -> dict:
    to_json: dict = loads(row_sting)

    pageid: dict = to_json['query']['pages']
    pageid = list(pageid.keys())[0]
    
    if pageid == '-1':
        " Article was not found. "
        return {'result': None}

    result: str = to_json['query']['pages'][pageid]['extract'].split('\n')[0]
    return {'result': result}


async def list_of_similar_article_titles(row_sting: str) -> dict:
    to_json: dict = loads(row_sting)
    search_results = list(d['title'] for d in to_json['query']['search'])
    if not search_results:
        return {}
    return {"articles": list(search_results)}
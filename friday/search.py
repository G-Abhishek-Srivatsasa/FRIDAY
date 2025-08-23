import wikipedia, requests

def wiki_search(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception:
        return None

def duckduckgo_query(query):
    try:
        url = "https://api.duckduckgo.com/"
        params = {"q": query, "format": "json"}
        res = requests.get(url, params=params).json()
        return res.get("AbstractText") or None
    except Exception:
        return None

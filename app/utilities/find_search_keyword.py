import re

def find_search_keyword(url):
    """
    Function to find search-keyword from URL

    Parameters
    ----------
    url : str
        URL of a web search.

    Returns
    -------
    str
         returns search keyword found in URL.

    """
    if 'google.com' in url:
        search_keyword = re.findall("&q=[a-zA-Z]+", url)[0][3:]
        return str(search_keyword).lower()
    
    if 'yahoo.com' in url:
        search_keyword = re.findall("\?p=[a-zA-z+,-]+", url)[0][3:]
        return str(search_keyword).lower()

    
    if 'bing.com' in url:
        search_keyword = re.findall("\?q=[a-zA-z+,-]+", url)[0][3:]
        return str(search_keyword).lower()
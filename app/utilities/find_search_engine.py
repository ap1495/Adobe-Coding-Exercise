def find_search_engine(url):
    """
    Function to find search engine from given URL

    Parameters
    ----------
    url : string
        url of a web search.

    Returns
    -------
    str
        Returns one of the three search engines if found in URL.

    """
    if 'google.com' in url:
        return 'google.com'
    
    if 'yahoo.com' in url:
        return 'yahoo.com'
    
    if 'bing.com' in url:
        return 'bing.com'
    
    return None
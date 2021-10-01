from app.utilities.find_search_keyword import find_search_keyword

def test_find_search_keyword_on_google_url():
    url = "http://www.google.com/search?hl=en&client=firefox-a&rls=org.mozilla%3Aen-US%3Aofficial&hs=ZzP&q=Ipod&aq=f&oq=&aqi="
    assert "ipod" == find_search_keyword(url)
    
def test_find_search_keyword_on_yahoo_url():
    url = "http://search.yahoo.com/search?p=cd+player&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-701"
    assert "cd+player" == find_search_keyword(url)
    
def test_find_search_keyword_on_bing_url():
    url = "http://www.bing.com/search?q=Zune&go=&form=QBLH&qs=n"
    assert "zune" == find_search_keyword(url)
    
def test_find_search_keyword():
    url = "http://www.xyz.com/search?hl=en&client=firefox-a&rls=org.mozilla%3Aen-US%3Aofficial&hs=ZzP&q=Ipod&aq=f&oq=&aqi="
    assert None == find_search_keyword(url)
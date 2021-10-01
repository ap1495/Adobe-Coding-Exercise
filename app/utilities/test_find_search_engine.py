from app.utilities.find_search_engine import find_search_engine

def test_find_search_engine_with_google():
    url = "http://www.google.com/search?hl=en&client=firefox-a&rls=org.mozilla%3Aen-US%3Aofficial&hs=ZzP&q=Ipod&aq=f&oq=&aqi="
    assert "google.com" == find_search_engine(url)
    
def test_find_search_engine_with_yahoo():
    url = "http://search.yahoo.com/search?p=cd+player&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-701"
    assert "yahoo.com" == find_search_engine(url)
    
def test_find_search_engine_with_bing():
    url = "http://www.bing.com/search?q=Zune&go=&form=QBLH&qs=n"
    assert "bing.com" == find_search_engine(url)
    
def test_find_search_engine():
    url = "http://www.xyz.com/search?hl=en&client=firefox-a&rls=org.mozilla%3Aen-US%3Aofficial&hs=ZzP&q=Ipod&aq=f&oq=&aqi="
    assert None == find_search_engine(url)
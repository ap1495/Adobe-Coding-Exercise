from app.solids.solid_get_search_engine import get_search_engine
from app.solids.solid_create_pyspark_df import create_pyspark_dataframe
from app.solids.solid_get_search_keyword import get_search_keyword

def test_get_search_keyword():
    file_path = "../adobe_data.tsv"
    delimiter = "\t"
    spark_app_name = "Test_Suite"
    new_column_name1 = "Search_Engine"
    new_column_name2 = "Search_Keyword"
    url_column = "referrer"
    df = create_pyspark_dataframe(file_path, delimiter, spark_app_name)
    df = get_search_engine(df, new_column_name1, url_column)
    df = get_search_keyword(df, new_column_name2, url_column)
    
    assert df.count() == 21
    assert len(df.columns) == 14
    assert new_column_name2 in list(df.columns)
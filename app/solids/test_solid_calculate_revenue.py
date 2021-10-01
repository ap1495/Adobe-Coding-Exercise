from app.solids.solid_get_search_engine import get_search_engine
from app.solids.solid_create_pyspark_df import create_pyspark_dataframe
from app.solids.solid_get_search_keyword import get_search_keyword
from app.solids.solid_calculate_revenue import calculate_revenue

def test_get_search_keyword():
    file_path = "C:/Users/sanja/Downloads/adobe_data.tsv"
    delimiter = "\t"
    spark_app_name = "Test_Suite"
    new_column_name1 = "Search_Engine"
    new_column_name2 = "Search_Keyword"
    new_column_name3 = "Revenue"
    event_list_column = "event_list"
    product_list_column = "product_list"
    url_column = "referrer"
    
    df = create_pyspark_dataframe(file_path, delimiter, spark_app_name)
    df = get_search_engine(df, new_column_name1, url_column)
    df = get_search_keyword(df, new_column_name2, url_column)
    df = calculate_revenue(df, new_column_name3, event_list_column, product_list_column)
    
    assert df.count() == 21
    assert len(df.columns) == 15
    assert new_column_name3 in list(df.columns)
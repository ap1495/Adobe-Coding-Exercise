from app.solids.solid_get_search_engine import get_search_engine
from app.solids.solid_create_pyspark_df import create_pyspark_dataframe

def test_get_search_engine():
    file_path = "../adobe_data.tsv"
    delimiter = "\t"
    spark_app_name = "Test_Suite"
    new_column_name = "Search_Engine"
    url_column = "referrer"
    df = create_pyspark_dataframe(file_path, delimiter, spark_app_name)
    df = get_search_engine(df, new_column_name, url_column)
    
    assert df.count() == 21
    assert len(df.columns) == 13
    assert new_column_name in list(df.columns)
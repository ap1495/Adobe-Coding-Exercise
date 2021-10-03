from app.solids.solid_get_search_engine import get_search_engine
from app.solids.solid_create_pyspark_df import create_pyspark_dataframe
from app.solids.solid_get_search_keyword import get_search_keyword
from app.solids.solid_calculate_revenue import calculate_revenue
from app.solids.solid_format_pyspark_df import format_pyspark_df_and_write_to_destination

def test_format_pyspark_df():
    file_path = "../adobe_data.tsv"
    delimiter = "\t"
    spark_app_name = "Test_Suite"
    new_column_name1 = "Search_Engine"
    new_column_name2 = "Search_Keyword"
    new_column_name3 = "Revenue"
    event_list_column = "event_list"
    product_list_column = "product_list"
    url_column = "referrer"
    output_folder = "output_files"
    groupby_column1 = "Search_Engine"
    groupby_column2 = "Search_Keyword"
    agg_column = "Revenue" 
    
    df = create_pyspark_dataframe(file_path, delimiter, spark_app_name)
    df = get_search_engine(df, new_column_name1, url_column)
    df = get_search_keyword(df, new_column_name2, url_column)
    df = calculate_revenue(df, new_column_name3, event_list_column, product_list_column)
    status = format_pyspark_df_and_write_to_destination(df, output_folder, delimiter, groupby_column1, groupby_column2, agg_column)
    
    assert status == "File successfully processed"
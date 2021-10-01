from app.solids.solid_create_pyspark_df import create_pyspark_dataframe

def test_solid_create_pyspark_df():
    file_path = "C:/Users/sanja/Downloads/adobe_data.tsv"
    delimiter = "\t"
    spark_app_name = "Test_Suite"
    df = create_pyspark_dataframe(file_path, delimiter, spark_app_name)
    assert df.count() == 21
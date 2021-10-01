from dagster import solid
import pyspark
from pyspark.sql import SparkSession

@solid
def create_pyspark_dataframe(file_path, delimiter, spark_app_name):
    """
    Solid to create pyspark dataframe using file path, file delimiter, and spark application name.

    Parameters
    ----------
    file_path : str
    delimiter : str
    spark_app_name : str

    Returns
    -------
    pyspark_df : Pyspark Dataframe
        Returns a pyspark dataframe after reading contents from file.

    """
    spark = SparkSession.builder.appName(spark_app_name).getOrCreate()
    pyspark_df = spark.read.option("header", "true").csv(file_path, sep=delimiter)
    return pyspark_df
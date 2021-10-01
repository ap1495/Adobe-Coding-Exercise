from orchestration_enums import TAB_FILE_DELIMITER

from dagster import solid
import pyspark
from pyspark.sql import SparkSession

@solid
def create_pyspark_dataframe(file_path):
    spark = SparkSession.builder.appName('RevenueCalculator').getOrCreate()
    pyspark_df = spark.read.option('header', 'true').csv(file_path, sep=TAB_FILE_DELIMITER)
    print(pyspark_df.show(2))
    return pyspark_df
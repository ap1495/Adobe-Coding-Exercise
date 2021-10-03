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
    spark.sparkContext._jsc.hadoopConfiguration.set("fs.s3a.access.key", "AKIAUF4F4O4JAH4O2T7H")
    spark.sparkContext._jsc.hadoopConfiguration.set("fs.s3a.secret.key", "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")
    spark.sparkContext._jsc.hadoopConfiguration.set("fs.s3a.endpoint", "s3://ap1495bucket")
    pyspark_df = spark.read.option("header", "true").csv("s3a://ap1495bucket/adobe_data.tsv", sep=delimiter)
    return pyspark_df
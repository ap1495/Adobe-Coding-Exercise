from dagster import solid
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

from app.utilities.find_search_keyword import find_search_keyword

@solid
def get_search_keyword(df):
    find_search_keyword_udf = udf(lambda x:find_search_keyword(x),StringType())
    df = df.withColumn("Search_Keyword", find_search_keyword_udf("referrer"))
    print(df.show(5, truncate=False))
    return df
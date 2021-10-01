from dagster import solid
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

from app.utilities.find_search_engine import find_search_engine

@solid
def get_search_engine(df):
    find_search_engine_udf = udf(lambda x:find_search_engine(x),StringType())
    df = df.withColumn("Search_Engine_Domain", find_search_engine_udf("referrer"))
    print(df.show(5))
    return df
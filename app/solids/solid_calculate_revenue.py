from dagster import solid
from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType

from app.utilities.calculate_total_revenue import calculate_total_revenue

@solid
def calculate_revenue(df):
    calculate_total_revenue_udf = udf(lambda x, y:calculate_total_revenue(x, y), FloatType())
    df = df.withColumn("Revenue", calculate_total_revenue_udf("event_list", "product_list"))
    print(df.show(20, truncate=False))
    return df
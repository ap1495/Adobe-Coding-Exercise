from dagster import solid
from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType
from app.utilities.calculate_total_revenue import calculate_total_revenue

@solid
def calculate_revenue(df, new_column_name, event_list_column_name, product_list_column_name):
    """
    Solid to calculate revenue from pyspark dataframe

    Parameters
    ----------
    df : Pyspark Dataframe
    new_column_name : str
    event_list_column_name : str
    product_list_column_name : str

    Returns
    -------
    df : Pyspark datafrome
        Returns a pyspark dataframe with revenue calculated for each product.

    """
    calculate_total_revenue_udf = udf(lambda x, y:calculate_total_revenue(x, y), FloatType())
    df = df.withColumn(new_column_name, calculate_total_revenue_udf(event_list_column_name, product_list_column_name))
    return df
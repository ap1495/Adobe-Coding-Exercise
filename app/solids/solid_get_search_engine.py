from dagster import solid
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

from app.utilities.find_search_engine import find_search_engine

@solid
def get_search_engine(df, new_column_name, url_column):
    """
    Solid to add a new column to pyspark dataframe that holds the search engine found.

    Parameters
    ----------
    df : Pyspark Dataframe
    new_column_name : str
    url_column : str

    Returns
    -------
    df : Pyspark Dataframe
        returns a pyspark dataframe with new column that stores search engine.

    """
    find_search_engine_udf = udf(lambda x:find_search_engine(x),StringType())
    df = df.withColumn(new_column_name, find_search_engine_udf(url_column))
    return df
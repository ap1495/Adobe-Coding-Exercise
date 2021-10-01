from dagster import solid
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

from app.utilities.find_search_keyword import find_search_keyword

@solid
def get_search_keyword(df, new_column_name, url_column):
    """
    Solid to add a new column to pyspark dataframe that holds the search keyword found.

    Parameters
    ----------
    df : Pyspark Dataframe
    new_column_name : str
    url_column : str

    Returns
    -------
    df : Pyspark Dataframe
        returns a pyspark dataframe with new column that stores search keyword.

    """
    find_search_keyword_udf = udf(lambda x:find_search_keyword(x), StringType())
    df = df.withColumn(new_column_name, find_search_keyword_udf(url_column))
    return df
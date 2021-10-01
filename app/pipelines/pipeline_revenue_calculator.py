from dagster import pipeline
from app.solids.solid_create_pyspark_df import create_pyspark_dataframe
from app.solids.solid_get_search_engine import get_search_engine
from app.solids.solid_get_search_keyword import get_search_keyword
from app.solids.solid_calculate_revenue import calculate_revenue

@pipeline
def calculate_revenue_pipeline():
    """
    Pipeline to calculate revnue from hit level data.

    Returns
    -------
    None.

    """
    pyspark_df = create_pyspark_dataframe()
    modified_pyspark_df_1 = get_search_engine(pyspark_df)
    modified_pyspark_df_2 = get_search_keyword(modified_pyspark_df_1)
    modified_pyspark_df_3 = calculate_revenue(modified_pyspark_df_2)
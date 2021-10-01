from dagster import solid
from datetime import date
from pyspark.sql.functions import col

@solid
def format_pyspark_df_and_write_to_destination(df, output_folder, output_file_delimiter, groupby_column1, groupby_column2, agg_column):
    """
    Solid to format pyspark dataframe and write to destination folder

    Parameters
    ----------
    df : Pyspark dataframe
    output_folder : str
    output_file_delimiter : str

    Returns
    -------
    str
        Returns a string if file has been successfully processed and written to destination folder.

    """
    sum_agg_column = "sum(" + agg_column + ")"
    final_pyspark_df = df.groupBy(groupby_column1, groupby_column2)\
    .sum(agg_column).withColumnRenamed(sum_agg_column, agg_column)\
    .na.drop("any").orderBy(col(agg_column).desc())
    
    final_pyspark_df.coalesce(1).write.mode("overwrite").option("sep", output_file_delimiter).csv(output_folder) 
    
    return "File successfully processed"
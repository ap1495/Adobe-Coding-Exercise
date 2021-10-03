from dagster import execute_pipeline
from datetime import date
from app.pipelines.pipeline_revenue_calculator import calculate_revenue_pipeline
from app_consts import SPARK_APP_NAME, TAB_FILE_DELIMITER
from app.file_types.file_types import BaseFileType

def calculate_revenue_app(file_path):
    """
    Function to trigger revenue calculator pipeline

    Parameters
    ----------
    file_path : str
        Path of the file from which revenue has to be calculated.

    Returns
    -------
    Pipeline execution status.

    """
    today_date = date.today()
    folder_name = "output_files/" + str(today_date) + "_SearchKeywordPerformance"
    
    file_type_obj = BaseFileType.initialize_file_type_obj("TAB")
    file_delimiter = file_type_obj.get_delimiter()
    
    run_config = {
        "solids": {
            "create_pyspark_dataframe": {
                "inputs": {
                    "file_path": {"value": file_path},
                    "delimiter": {"value": file_delimiter},
                    "spark_app_name": {"value": SPARK_APP_NAME}
                    }
                },
            "get_search_engine": {
                "inputs": {
                    "new_column_name": {"value": "Search_Engine_Domain"},
                    "url_column": {"value": "referrer"}
                    }
                },
            "get_search_keyword": {
                "inputs": {
                    "new_column_name": {"value": "Search_Keyword"},
                    "url_column": {"value": "referrer"}
                    }
                },
            "calculate_revenue": {
                "inputs": {
                    "new_column_name": {"value": "Revenue"},
                    "event_list_column_name": {"value": "event_list"},
                    "product_list_column_name": {"value": "product_list"}
                    }
                },
            "format_pyspark_df_and_write_to_destination": {
                "inputs": {
                    "output_folder": {"value": folder_name},
                    "output_file_delimiter": {"value": TAB_FILE_DELIMITER},
                    "groupby_column1": {"value": "Search_Engine_Domain"},
                    "groupby_column2": {"value": "Search_Keyword"},
                    "agg_column": {"value": "Revenue"}
                    }
                }
            }
        }
    pipeline_result = execute_pipeline(pipeline=calculate_revenue_pipeline, run_config=run_config)
    
    return "Calculate_Revenue_Pipeline_Success_Status: " + str(pipeline_result.success)
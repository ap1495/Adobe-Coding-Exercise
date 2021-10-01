from dagster import execute_pipeline
from app.pipelines.pipeline_revenue_calculator import calculate_revenue_pipeline

def calculate_revenue_app(file_path):
    print(file_path)
    run_config = {
        "solids": {
            "create_pyspark_dataframe": {
                "inputs": {
                    "file_path": {"value": file_path}
                    }
                }
            }
        }
    pipeline_result = execute_pipeline(pipeline=calculate_revenue_pipeline, run_config=run_config)
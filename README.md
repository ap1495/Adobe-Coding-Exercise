# Adobe-Coding-Exercise

The goal of this project is to build an application to calculate revenue that the client is generating from external search engines, by processing hit level data files. The hit level data files are in the form of tab delimited files. These data files are processed and an output file is generated that stores the Search Engine Domain, Search Keyword, and Revenue.

# Programming Language:
- Python

# Libraries:
- Dagit
- Dagster
- PySpark
- Pytest

# To run this application:
- python3 main.py <- path of file to be processed ->

![image](https://user-images.githubusercontent.com/35802181/135767568-42c06c20-0566-4f62-90a2-4c5699f9b288.png)

  
# To run the test suite:
- python3 -m pytest app/

![image](https://user-images.githubusercontent.com/35802181/135767585-c5d6c485-355b-4d5b-9759-8dde3529bfc4.png)


# To view the pipeline execution on Dagit UI:
- dagit -f <- path of the pipeline file ->

![image](https://user-images.githubusercontent.com/35802181/135767620-b253a48e-49ae-43c9-8c88-cd9a5b79aa90.png)


# Deployment to an EC2 instance:
- Spin up a free tier eligible EC2 instance.
- Download and install Python, Java, and Spark.
- pip install pyspark dagster dagit pytest
- Run python application.
![image](https://user-images.githubusercontent.com/35802181/135770424-48c65dcc-f086-4b70-8b11-cc969f4d07db.png)

# Deliverables:
- Upon processing the hit level data file, an output file is generated at the path output_file/[Date]_SearchKeywordPerformance/ where [Date] is the date on which the application processed the hit level data file.

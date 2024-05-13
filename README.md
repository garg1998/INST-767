# GCP DATA PIPELINE
This project fetches the latest data for 4 tech companies, and 4 pharmaceutical and 4 Financial companies using Yahoo Polygon API, Tiingo API, and Alpha Vantage API in batch format storing the raw data to Google storage. Google Schedular which is scheduled to run daily, updates the data in cloud storage. ETL transformations are performed using the DataProc PySpark cluster and the processed data is then loaded into BigQuery. Google workflow was used to automate the Transformation and loading part, scheduled to run daily. Finally, sample queries were written in Bigquery to answer some proposed business questions related to the loaded stock data

# Techonologies Used
* Google Cloud Platform
* Alpha Vantage API
* Polygon API
* Tiingo API
* Pyspark
* DataProc
* Bigquery
* SQL

# Architecture

<img width="933" alt="image" src="https://github.com/garg1998/INST-767/assets/48328700/532ae1f2-49d2-4fc8-b3f7-485ebc5c9830">



## Ingestion
Data is being extracted from 3 APIs namely Alphavantage API, Polygon API, Tiingo API. Alphavantage API is being used to extract daily stock
prices for financial companies ( limited to 4 for the project), Tiingo is used to extract daily stock prices for Healthcare companies and Polygon API is used to extract daily stock prices for Tech companies. Cloud Functions are used to perform the extraction. The extracted data is then stored in JSON format in Google Cloud Storage. The whole process is scheduled to run on daily basis using cloud scheduler

<img width="1345" alt="image" src="https://github.com/garg1998/INST-767/assets/48328700/3aa51947-cdd1-4111-b907-17de179580ca">

<img width="1439" alt="image" src="https://github.com/garg1998/INST-767/assets/48328700/3371787d-3fd4-4841-924e-448757bcc094">

<img width="1467" alt="image" src="https://github.com/garg1998/INST-767/assets/48328700/f11f12c9-d4b1-4da8-bb81-8365a0bee4dc">




## Transformation

The data stored in Google Storage is then transformed into the right format using Dataproc and Spark jobs. After transformation, the final result is stored in Google BigQuery. The transformation process is scheduled to run daily using Google workflow, transforming the daily ingested data and appending the result into the big query

<img width="1175" alt="image" src="https://github.com/garg1998/INST-767/assets/48328700/a58f1bed-22c4-4f53-8fe1-06c0f3c89895">

<img width="1216" alt="image" src="https://github.com/garg1998/INST-767/assets/48328700/d42cc248-a79b-4ce1-a515-8e2678fc9497">



## Storage
The transformed data is then stored in BigQuery. The data is stored in three tables: Tech, Finance, and Healthcare
<img width="1012" alt="image" src="https://github.com/garg1998/INST-767/assets/48328700/853f38ba-8dfd-4ce5-b0ad-31742bceac07">

## Analysis
For analysis, a seperate analysis for each sector was conducted and then 4 sample business questions were formulated comparing all the sectors and the data was queried using SQL in BigQuery to get the desired data
<img width="613" alt="image" src="https://github.com/garg1998/INST-767/assets/48328700/c8566b0a-b523-44a2-ad54-b5a71c81d2f1">

<img width="733" alt="image" src="https://github.com/garg1998/INST-767/assets/48328700/3a9418a4-0cae-42cb-b3cc-c796a49ad441">








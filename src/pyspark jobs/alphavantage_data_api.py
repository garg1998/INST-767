# Import Libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from google.cloud import bigquery
from pyspark.sql.types import *
import pyspark.sql.functions as F
from google.cloud.exceptions import NotFound
import pandas as pd

# Create a Spark session
spark = SparkSession.builder \
                    .appName('alpha_vantage_api') \
                    .getOrCreate()

# Intialize below
bucket = "alphavantagestorage"
project_id = "adroit-archive-422123-h0"
dataset_id = "stockdata"
table_id='finance'

# json file name
today=pd.to_datetime('today').date()
file_name='stock_data'+str(today)+'.json'
file=f'gs://alphavantagestorage/{file_name}'


# Read the JSON file into a DataFrame
df = spark.read.json(file)

# Print the schema of the DataFrame
print("Schema of the DataFrame:")
df.printSchema()

# Data Cleaning and Transformation

# changing column names
new=["Open", "High",'Low','Close','Volume','Date']
for c,n in zip(df.columns,new):
    df=df.withColumnRenamed(c,n)

# changing data types
df = df.withColumn("Open", df["Open"].cast("float"))
df = df.withColumn( "High", df["High"].cast("float"))
df = df.withColumn('Low', df["Low"].cast("float"))
df = df.withColumn('Close', df["Close"].cast("float"))
df = df.withColumn('Volume', df["Volume"].cast("int"))
df = df.withColumn('Date',F.to_date(df["Date"], "yyyy-MM-dd"))

# add a column doing average 
df_new = df.withColumn('average', (col('Close') + col('High')) / 2.0)
df_clean = df_new.withColumn('average', col('average').cast(DoubleType()))

df_clean.show()


# Initialize 
client = bigquery.Client()

# check if dataset exists

try:
    client.get_dataset(dataset_id)  # Make an API request.
    print("Dataset {} already exists".format(dataset_id))
except NotFound:
    dataset.location = "US"
    dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
    print("Created dataset {}.{}".format(project_id, dataset.dataset_id))
    


# Write the DataFrame to BigQuery with autodetected schema
df_clean.write.format('bigquery') \
    .option('table', 'adroit-archive-422123-h0.stockdata.finance') \
    .option('temporaryGcsBucket', bucket) \
    .mode('append') \
    .save()

# Stop the Spark session
spark.stop()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import *
import pandas as pd




current_year = 2023
# Initialize a Spark session
spark = SparkSession.builder.appName("FilterCost").getOrCreate()
spark.conf.set('temporaryGcsBucket', "mini-projet-bucket")

# Read the CSV file into a DataFrame
csv_path = "gs://mini-projet-bucket/Crimes_-_2001_to_Present.csv"

df = spark.read.csv(csv_path, header=True, inferSchema=True)

df = df.withColumn("Year", col("Date").substr(7, 4))
df = df.withColumn("Month", col("Date").substr(1, 2))

# Convertir les colonnes en entier
df = df.withColumn("Year", col("Year").cast("int"))
df = df.withColumn("Month", col("Month").cast("int"))

df = df.withColumn("Date", to_timestamp(col("Date"), "MM/dd/yyyy hh:mm:ss a"))
#df = df.withColumn("Updated On", to_timestamp(col("Updated On"), "MM/dd/yyyy hh:mm:ss a"))

df = df.drop('Block', 'IUCR', 'X Coordinate', 'Y Coordinate', 'Updated On', 'Latitude', 'Longitude', 'Location')

df_cleaned = df.select([col("" + c + "").alias(c.replace(' ', '').replace('.', '').replace('/', '')) for c in df.columns])



df_cleaned.write.format("bigquery").option("table","civic-origin-407810.architecture2.data").mode("overwrite").save()


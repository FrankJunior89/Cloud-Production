from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import *

current_year = 2023
# Initialize a Spark session
spark = SparkSession.builder.appName("FilterCost").getOrCreate()

# Read the CSV file into a DataFrame
csv_path = "gs://mini-projet-bucket/Crimes_-_2001_to_Present.csv"

df = spark.read.csv(csv_path, header=True, inferSchema=True)

df = df.withColumn("Year", col("Date").substr(7, 4))
df = df.withColumn("Month", col("Date").substr(1, 2))

# Convertir les colonnes en entier
df = df.withColumn("Year", col("Year").cast("int"))
df = df.withColumn("Month", col("Month").cast("int"))

df = df.withColumn("Date", to_timestamp(col("Date"), "MM/dd/yyyy hh:mm:ss a"))

df = df.withColumn("Date", col("Date") + expr("INTERVAL 3 YEARS"))
#df = df.withColumn("Updated On", to_timestamp(col("Updated On"), "MM/dd/yyyy hh:mm:ss a"))

df = df.drop('Block', 'IUCR', 'X Coordinate', 'Y Coordinate', 'Updated On', 'Latitude', 'Longitude', 'Location')



df1 = df.filter((df["Year"] >= current_year - 4) & (df["Year"] <= current_year))
df2 = df.filter((df["Year"] >= current_year - 2) & (df["Year"] <= current_year) & (df["Primary Type"] == "THEFT"))
df3 = df.groupBy(["Year"]).count()
df5 = df.filter((df["Year"] >= 2016) & (df["Year"] <= 2019) & (df["arrest"] == "true"))




output_csv_path1 = "gs://bucket-ouput/outputs1"
output_csv_path2 = "gs://bucket-ouput/outputs2"
output_csv_path3 = "gs://bucket-ouput/outputs3"
output_csv_path4 = "gs://bucket-ouput/outputs4"
output_csv_path5 = "gs://bucket-ouput/outputs5"

df1.coalesce(1).write.csv(output_csv_path1, header=True, mode="overwrite")
df2.coalesce(1).write.csv(output_csv_path2, header=True, mode="overwrite")
df3.coalesce(1).write.csv(output_csv_path3, header=True, mode="overwrite")
df5.coalesce(1).write.csv(output_csv_path5, header=True, mode="overwrite")

#df.write.format("bigquery").option("table","civic-origin-407810.architecture2.data").mode("overwrite").save()

spark.stop()



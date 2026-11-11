from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pandas import *
# sem querys

spark = SparkSession.builder.getOrCreate()

dataset = spark.read.csv("california_housing_test.csv", inferSchema= True, header= True)
dataset.printSchema()

dataset.count()

dataset.createOrReplaceTempView("tabela_temporaria")

dataset.select("logitude", "latitude").show(3)

max_rooms = dataset.select(F.max("total_rooms")).collect()[0][0]
print(f"Máximo de quartos: {max_rooms}")

# print(spark.catalog.listTables())

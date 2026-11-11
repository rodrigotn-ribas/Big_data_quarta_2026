from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pandas import *
# sem querys

spark = SparkSession.builder.getOrCreate()

dataset = spark.read.csv("california_housing_test.csv", inferSchema= True, header= True)
dataset.printSchema()

# dataset.count()

dataset.createOrReplaceTempView("tabela_temporaria")

dataset.select("longitude", "latitude").show(3)

max_rooms = dataset.select(F.max("total_rooms")).collect()[0][0]
# print(f"Máximo de quartos: {max_rooms}")

dataset = dataset.withColumn("rooms_per_household", dataset["total_rooms"] /
                             dataset["households"])
dataset.filter(dataset["median_income"] > 5).show()

dataset.groupBy("housing_median_age").avg("median_house_value").sort("housing_median_age").show()

# print(spark.catalog.listTables())

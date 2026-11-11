from pyspark.sql import SparkSession
from pandas import *
# com querys

spark = SparkSession.builder.getOrCreate()

dataset = spark.read.csv("california_housing_test.csv", inferSchema= True, header= True)
dataset.printSchema()

dataset.count()

dataset.createOrReplaceTempView("tabela_temporaria")

query_spark = "SELECT MAX(total_rooms) as maximo_quartos FROM tabela_temporaria"
q_maximo_quartos = spark.sql(query_spark)
pd_maximo_quartos = q_maximo_quartos.toPandas()

print(f"A quantidade máxima de quartos é: {pd_maximo_quartos["maximo_quartos"]}")
qtd_maximo_quartos = int(pd_maximo_quartos.loc[0, "maximo_quartos"])

# print(spark.catalog.listTables())

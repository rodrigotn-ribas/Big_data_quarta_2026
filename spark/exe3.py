from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
query = "FROM tabela_temporaria SELECT longitude, latitude LIMIT 3"

dataset = spark.read.csv("california_housing_test.csv", inferSchema= True, header= True)
dataset.printSchema()

dataset.count()

dataset.createOrReplaceTempView("tabela_temporaria")

saida = spark.sql(query)
saida.show()

# print(spark.catalog.listTables())

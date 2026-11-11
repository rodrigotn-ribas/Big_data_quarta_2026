
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, desc

spark = SparkSession.builder.appName("Varejo_Analytics").getOrCreate()




dados = [("RJ", "Eletrônicos", 1500.00), ("SP", "Roupas", 200.00),
         ("RJ", "Eletrônicos", 3000.00), ("MG", "Livros", 50.00)]
colunas = ["Estado", "Categoria", "Valor"]

df_transacoes = spark.createDataFrame(dados, colunas)
print(df_transacoes)

resultado_agrupado = df_transacoes.groupBy("Estado", "Categoria") \
    .agg(sum("Valor").alias("Receita_Total")) \
    .orderBy(desc("Receita_Total"))

resultado_agrupado.show()

dataset = spark.read.csv("california_housing_test.csv", inferSchema= True, header= True)
dataset.printSchema()

spark.stop()



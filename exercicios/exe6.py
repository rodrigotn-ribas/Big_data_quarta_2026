from pyspark.sql import functions as F

df = {}

resumo = (
    df
    .filter(F.col("valor") > 0)
    .groupBy("regiao")
    .agg(
        F.sum("valor").alias("faturamento"),
        F.count("*").alias("registros")
    )
    .orderBy(F.desc("faturamento"))
)

resumo.show
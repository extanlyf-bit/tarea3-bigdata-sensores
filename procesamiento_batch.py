from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, sum, when

# 1. Iniciar Spark
spark = SparkSession.builder \
    .appName("AnalisisSensoresIoT") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")
# 2. Cargar los datos
ruta = "/home/vboxuser/tarea3_bigdata/datos/sensor_data.csv"

df = spark.read.option("header", True) \
    .option("inferSchema", True).csv(ruta)

print("Datos originales:", df.count())
df.show(5, truncate=False)

# 3. Limpiar datos
df = df.dropna(subset=["timestamp", "sensor", "value"])
df = df.dropDuplicates()

print("Datos limpios:", df.count())

# 4. Analizar anomalías por sensor
resumen = df.groupBy("sensor").agg(
    count("*").alias("total_registros"),
    sum(when(col("is_anomaly") == 1, 1).otherwise(0))
        .alias("total_anomalias"),
    count(col("fault_type")).alias("registros_con_falla"),
    avg("value").alias("valor_promedio")
)

resumen.orderBy(col("registros_con_falla").desc()).show(
    truncate=False
)

# 5. Guardar resultados
salida = "/home/vboxuser/tarea3_bigdata/resultados/resumen_sensores"

resumen.coalesce(1).write.mode("overwrite") \
    .option("header", True).csv(salida)

print("Analisis terminado. Resultados guardados en:", salida)

spark.stop()

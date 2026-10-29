
import csv
import glob
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Ubicacion de los resultados generados por Spark
carpeta = "/home/vboxuser/tarea3_bigdata/resultados/resumen_sensores"
archivos = glob.glob(os.path.join(carpeta, "part-*.csv"))

if not archivos:
    raise FileNotFoundError(
        "No se encontro el CSV de resultados de Spark."
    )

sensores = []
anomalias = []

# Leer el resumen por sensor
with open(archivos[0], newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        sensores.append(fila["sensor"])
        anomalias.append(int(fila["total_anomalias"]))

# Crear la grafica de barras
plt.figure(figsize=(12, 7))
barras = plt.bar(sensores, anomalias)

plt.title("Anomalias detectadas por sensor IoT")
plt.xlabel("Sensor")
plt.ylabel("Cantidad de anomalias")
plt.xticks(rotation=45, ha="right")
plt.bar_label(barras, padding=3)
plt.tight_layout()

# Guardar la imagen
salida = "/home/vboxuser/tarea3_bigdata/resultados/anomalias_por_sensor.png"
plt.savefig(salida, dpi=150)
plt.close()

print("Grafica guardada en:", salida)
print("Total de anomalias:", sum(anomalias))

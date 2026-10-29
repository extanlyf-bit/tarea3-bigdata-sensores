# Análisis de datos de sensores IoT con Apache Spark

## 1. Descripción del proyecto

Este proyecto realiza el procesamiento por lotes (Batch) de un conjunto de datos de sensores IoT para identificar anomalías y obtener estadísticas por sensor mediante Apache Spark y PySpark.

También incluye un script para visualizar los resultados mediante una gráfica de barras.

## 2. Fuente de los datos

Dataset: [IoT Sensor Data for Anomaly Detection](https://www.kaggle.com/datasets/mmunawarabbas/iot-sensor-data-for-anomaly-detection)

El archivo utilizado es `sensor_data.csv`, que contiene registros de diferentes sensores, sus mediciones, estados de máquina y etiquetas de anomalía.

## 3. Archivos del proyecto

- `procesamiento_batch.py`: carga los datos, realiza limpieza, elimina duplicados y calcula estadísticas y anomalías por sensor.
- `graficar_anomalias.py`: lee el resumen generado por Spark y crea una gráfica de barras con las anomalías detectadas.

## 4. Tecnologías utilizadas

- Python 3.10
- Apache Spark 3.5.8
- PySpark
- Matplotlib 3.10.9
- Dataset de sensores IoT en formato CSV

## 5. Resultados obtenidos

En la ejecución realizada se procesaron 172.800 registros correspondientes a 10 sensores y se identificaron 6.731 anomalías.

El resumen estadístico se guardó en la carpeta `resultados/resumen_sensores` y la gráfica se generó como `resultados/anomalias_por_sensor.png`.

## 6. Instrucciones de ejecución

### Procesamiento por lotes

1. Descargar el conjunto de datos desde la fuente original.
2. Guardar el archivo `sensor_data.csv` en la carpeta `datos` del proyecto.
3. Verificar la ruta del archivo CSV dentro de `procesamiento_batch.py`.
4. Ejecutar el procesamiento desde Ubuntu con:

```bash
/opt/spark/bin/spark-submit ~/tarea3_bigdata/procesamiento_batch.py
```

### Generación de la gráfica

Verificar que Matplotlib esté instalado y que el procesamiento batch haya generado el archivo CSV de resultados. Luego ejecutar:

```bash
python3 ~/tarea3_bigdata/graficar_anomalias.py
```

La gráfica se guardará en la carpeta de resultados indicada en el script.

## 7. Observación

Los resultados corresponden a una ejecución del conjunto de datos utilizado en esta práctica. El procesamiento por lotes es independiente del flujo de procesamiento en tiempo real con Kafka y Spark Streaming.

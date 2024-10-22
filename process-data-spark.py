from pyspark.sql import SparkSession

# Inicia uma sessão Spark
spark = SparkSession.builder.appName('DataPipeline').getOrCreate()

# Lê o CSV no Spark
df_spark = spark.read.csv('sales_data.csv', header=True, inferSchema=True)

# Realiza uma operação de agregação
df_spark.groupBy('Country').sum('TotalConfirmed').show()

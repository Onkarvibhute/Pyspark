from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("MyFirstPySparkApp")
    .master("local[*]")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35),
]

df = spark.createDataFrame(data, ["name", "age"])

df.show()

spark.stop()

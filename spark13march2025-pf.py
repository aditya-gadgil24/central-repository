# SHREE

# Data processing, transformation, logic using Apache Spark framework

# code block
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkTest").getOrCreate()
print(spark)


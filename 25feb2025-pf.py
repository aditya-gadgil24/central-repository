# Shree

# Spark codes

# begin
from pyspark import SparkConf
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("MySparkApp") \
    .getOrCreate()

data = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(data)

squared_rdd = rdd.map(lambda x: x * x)  # Transformation

filtered_rdd = squared_rdd.filter(lambda x: x > 10)  # Transformation

result = filtered_rdd.collect()  # Action

print(result)  # Output: [16, 25]

# end
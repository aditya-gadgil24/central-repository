# code 01
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("LazyEvaluationExample").getOrCreate()

data = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(data)

# Transformations (lazy)
squared_rdd = rdd.map(lambda x: x * x)
filtered_rdd = squared_rdd.filter(lambda x: x > 10)

# No computation has occurred yet!

# Action (triggers execution)
result = filtered_rdd.collect()

print(result)  # Output: [16, 25]

spark.stop()
# end of code
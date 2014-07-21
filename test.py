from pyspark import SparkContext

sc = SparkContext("local")
test = sc.parallelize(range(5))
test.collect().collect()



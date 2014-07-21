from pyspark import SparkContext

sc = SparkContext("local")
test = sc.parallelize(range(5))
test.map(lambda x: (x, 1)).collect()



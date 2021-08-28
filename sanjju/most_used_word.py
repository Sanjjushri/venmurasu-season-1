import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.types import  StringType
import pyspark.sql.functions as f
import csv
import matplotlib.pyplot as plt

spark = SparkSession.builder.appName('pandasToSparkDF').getOrCreate()

pdDF = pd.read_csv("../datasets/முதற்கனல்.csv")



mySchema = StructType([ StructField("Col1", StringType(), True)])

df = spark.createDataFrame(pdDF,schema=mySchema)

df= df.withColumn('word', f.explode(f.split(f.col('Col1'), ' '))) \
            .groupBy('word') \
            .count() \
            .sort('count', ascending=False) 
            #.show() 
df.toPandas().to_csv('../datasets/முதற்கனல்_4.csv')


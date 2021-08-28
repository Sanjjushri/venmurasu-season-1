import pyspark
import pandas as pd
import numpy as np
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import SparkSession

from datetime import datetime, date
import pandas as pd
from pyspark.sql.functions import udf, split, col
from pyspark.sql.types import IntegerType, StringType
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('pandasToSparkDF').getOrCreate()

pdDF = pd.read_csv("../datasets/முதற்கனல்.csv")

mySchema = StructType([ StructField("Col1", StringType(), True)])

df = spark.createDataFrame(pdDF,schema=mySchema)

df=df.withColumn('word', f.explode(f.split(f.col('Col1'), ' '))) \
     .groupBy('word') \
     .count() \
     .sort('count', ascending=True) 
  #.show()
df.toPandas().to_csv('../datasets/முதற்கனல்_5.csv')



import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import SparkSession
import csv
from datetime import datetime, date
import pandas as pd
from pyspark.sql.functions import udf, split, col
from pyspark.sql.types import IntegerType, StringType
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('pandasToSparkDF').getOrCreate()

pdDF = pd.read_csv("முதற்கனல்.csv")



mySchema = StructType([ StructField("Col1", StringType(), True)])

df = spark.createDataFrame(pdDF,schema=mySchema)

def get_data():

    df = pd.read_csv('../datasets/முதற்கனல்.csv')
    
    return df

def startpy():

    df = spark.createDataFrame(get_data())

    df.createOrReplaceTempView("data")

    df_result = spark.sql("SELECT column1 \
                           FROM data")

    df_result = df_result.withColumn("wordCount", f.size(f.split(f.col("column1"), " ")))

    df_result.select(f.sum("wordCount")).collect()

    df_result.show()

    df_result.toPandas().to_csv('../datasets/முதற்கனல்_2.csv')

if __name__== "__main__":
    startpy()

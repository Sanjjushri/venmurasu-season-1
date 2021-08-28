from pyspark.sql import SparkSession
import csv
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql.functions import udf, split, col
from pyspark.sql.types import IntegerType, StringType
import pyspark.sql.functions as f
from pyspark.sql.types import *

spark = SparkSession.builder.getOrCreate()

pdDF = pd.read_csv("../datasets/முதற்கனல்.csv")

mySchema = StructType([ StructField("Col1", StringType(), True)])

df = spark.createDataFrame(pdDF,schema=mySchema)


def get_data():
    
    df = pd.read_csv('../datasets/முதற்கனல்.csv')

    return df

def startpy():
    
    df = spark.createDataFrame(get_data())

    df.createOrReplaceTempView("venmurasu")

    df_result =  spark.sql("SELECT column1\
                            FROM venmurasu")
                            
    df_result.filter( (df.column1  == "பகுதி ஒன்று : வேள்விமுகம்") ) \
        .show(truncate=False)  

    df_result.toPandas().to_csv('../datasets/முதற்கனல்_3.csv')

if __name__ == '__main__':
    startpy()

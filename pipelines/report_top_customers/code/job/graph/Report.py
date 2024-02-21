from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Report(spark: SparkSession, in0: DataFrame):
    if Config.fabricName == "dev":
        in0.write\
            .option("header", True)\
            .option("sep", ",")\
            .option("ignoreLeadingWhiteSpace", True)\
            .option("ignoreTrailingWhiteSpace", True)\
            .mode("overwrite")\
            .option("separator", ",")\
            .option("header", True)\
            .csv("dbfs:/Prophecy/62b68c989346fb73b99043b4479d02a0/report-top-customers.csv")
    else:
        raise Exception("No valid dataset present to read fabric")

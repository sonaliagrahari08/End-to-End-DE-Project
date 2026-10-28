# Databricks notebook source
# MAGIC %md
# MAGIC #### load all mapping table from ADLS into Pandas and convert pandas Dataframe into spark Datframe

# COMMAND ----------

# DBTITLE 1,Ingest raw JSON files to bronze
import pandas as pd
files= [{"file":"map_cities"},
        {"file":"map_cancellation_reasons"},
        {"file":"bulk_rides"},
        {"file":"map_payment_methods"},
        {"file":"map_ride_statuses"},
        {"file":"map_vehicle_makes"},
        {"file":"map_vehicle_types"}]
 
for file in files:
    url = f"https://uberstoracc.blob.core.windows.net/raw/git/{file["file"]}.json?sp=r&st=2026-10-25T13:37:27Z&se=2026-10-26T21:52:27Z&spr=https&sv=2026-02-06&sr=c&sig=TWFbQZ81BZF52R4B5MKO8eAhEjGogA%2F5ks1r%2FtTVA4Y%3D"

    df = pd.read_json(url)
# create spark dataframe
    spark_df = spark.createDataFrame(df)
# write to delta table
    spark_df.write.format("delta")\
             .mode("overwrite")\
             .option("overwriteSchema",True)\
             .saveAsTable(f"uber.bronze.{file["file"]}")
     



# COMMAND ----------


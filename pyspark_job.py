from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def clean_data(df: DataFrame) -> DataFrame:
    """تنظيف البيانات وإزالة القيم الفارغة وتنسيق النصوص."""
    return df.dropna().withColumn("name", F.trim(F.col("name")))
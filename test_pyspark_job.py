import pytest
from pyspark.sql import SparkSession
from pyspark_job import clean_data


@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("PySparkTests")
        .getOrCreate()
    )
    yield spark
    spark.stop()


def test_clean_data(spark):
    data = [(" Alice ", 25), ("Bob", None), (None, 30)]
    columns = ["name", "age"]

    df = spark.createDataFrame(data, columns)
    cleaned_df = clean_data(df)

    results = cleaned_df.collect()

    assert len(results) == 1
    assert results[0]["name"] == "Alice"
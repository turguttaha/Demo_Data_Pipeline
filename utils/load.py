from dotenv import load_dotenv
import pandas as pd
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

load_dotenv()

token = os.getenv("INFLUXDB_TOKEN")
org = os.getenv("INFLUXDB_ORG")
url = os.getenv("INFLUXDB_URL")


client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "Demo_Data_Pipeline"

write_api = client.write_api(write_options=SYNCHRONOUS)


def load_data(df: pd.DataFrame):
    for index, row in df.iterrows():
        point = (
            Point("amsterdam_measurement")
            .tag("location", row["location"])
            .tag("unit", row["unit"])
            .field(row["parameter"], row["value"])
        )
        write_api.write(bucket=bucket, org=org, record=point)

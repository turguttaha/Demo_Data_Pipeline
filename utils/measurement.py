import pandas as pd
from utils.models import City


async def get_avg_per_location(city: City) -> pd.DataFrame:
    measurements = await city.get_measurements()
    df = pd.DataFrame(measurements)
    avg_per_location = (
        df.groupby(["locationId", "location", "parameter", "unit"])["value"]
        .mean()
        .reset_index()
    )
    return avg_per_location


def get_avg_of_the_city(avg_per_location_df: pd.DataFrame) -> pd.DataFrame:
    avg_city = (
        avg_per_location_df.groupby(["parameter", "unit"])["value"].mean().reset_index()
    )
    avg_city["locationId"] = 0
    avg_city["location"] = "Amsterdam-General"
    return avg_city


def include_avg_of_the_city(
    avg_per_location_df: pd.DataFrame, avg_city: pd.DataFrame
) -> pd.DataFrame:
    final_df = pd.concat([avg_per_location_df, avg_city], ignore_index=True)
    return final_df

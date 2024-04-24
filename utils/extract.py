import httpx
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
api_key = os.getenv("api_key")

headers = {"X-API-Key": api_key, "accept": "application/json"}
session = httpx.AsyncClient(headers=headers)


async def get_last_2day_measurements(
    city: str,
) -> list:
    current_datetime = datetime.now()
    datetime_24_hours_ago = current_datetime - timedelta(hours=48)
    result = await get_measurements(
        city=city, date_from=datetime_24_hours_ago, date_to=current_datetime
    )
    return result


async def get_measurements(city: str, date_from: datetime, date_to: datetime) -> list:
    # Convert datetime object to string with timezone offset
    to_datetime_str = date_to.strftime("%Y-%m-%dT%H:%M:%S%z")
    before_datetime_str = date_from.strftime("%Y-%m-%dT%H:%M:%S%z")
    # Replace characters with URL-encoded equivalents
    to_datetime_str_encoded = to_datetime_str.replace(":", "%3A").replace("+", "%2B")
    before_datetime_str_encoded = before_datetime_str.replace(":", "%3A").replace(
        "+", "%2B"
    )
    url = f"https://api.openaq.org/v2/measurements?date_from={before_datetime_str_encoded}&date_to={to_datetime_str_encoded}&limit=1000&page=1&offset=0&sort=desc&radius=1000&city={city}&order_by=datetime"
    response = await session.get(url=url)
    result = response.json()
    result = result["results"]
    return result

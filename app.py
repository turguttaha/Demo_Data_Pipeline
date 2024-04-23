import argparse
import asyncio
from utils.compute_measurements import compute


async def compute_measurements(params):
    city_name = params.city_name
    if type(city_name) is str:
        city_name = city_name.upper()
        print(f"computation is started for {city_name}")
        await compute(city_name=city_name)
        print(f"computation is completed for {city_name}")
    else:
        print("city name should be string!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest data to etl image")
    parser.add_argument("--city_name", required=True, help="city name")
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(compute_measurements(args))]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

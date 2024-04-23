from utils.load import load_data
from utils.models import City
from utils.measurement import (
    get_avg_of_the_city,
    get_avg_per_location,
    include_avg_of_the_city,
)


async def compute(city_name: str):
    city = City(name=city_name)
    await city.initialize_measurements()
    if city.get_measurements() is not None:
        print("Data is extacted!")
    avg_per_location = await get_avg_per_location(city=city)
    print("avg_per_location calculated!")
    avg_of_the_city = get_avg_of_the_city(avg_per_location)
    print("avg_city calculated!")
    df_to_load = include_avg_of_the_city(
        avg_per_location_df=avg_per_location, avg_city=avg_of_the_city
    )
    print("avg_city inclueded !")
    load_data(df=df_to_load)
    print("data is loaded !")

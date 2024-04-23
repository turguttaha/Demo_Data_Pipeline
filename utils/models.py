from utils.extract import get_last_day_measurements


class City:
    def __init__(self, name):
        self.name = name
        self.measurements = None

    async def initialize_measurements(self):
        self.measurements = await get_last_day_measurements(self.name)

    async def get_measurements(self):
        if self.measurements is None:
            await self.initialize_measurements()
        return self.measurements

import python_weather
import asyncio
import os

import time

while True:
    async def getweather():
        # declare the client. format defaults to the metric system (celcius, km/h, etc.)
        async with python_weather.Client(format=python_weather.IMPERIAL) as client:

            # fetch a weather forecast from a city
            weather = await client.get('Kuiv, Ukraine')
            weather_cel = (weather.current.temperature - 32) / 1.8
            time.sleep(10)
            if weather.current.temperature > weather.current.temperature:
                print('Attantion! Weather has changed PLUS')
            if weather.current.temperature > weather.current.temperature:
                print('Attantion! Weather has changed MINUS ')

            # returns the current day's forecast temperature (int)
            print('Температура в Киеве: ',weather_cel,'°')

    if __name__ == "__main__":
        if os.name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        asyncio.run(getweather())
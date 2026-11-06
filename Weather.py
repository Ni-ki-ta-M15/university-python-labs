# import python_weather
# import asyncio
# import os
#
#
# async def getweather():
#     async with python_weather.Client(format=python_weather.IMPERIAL) as client:
#         city = input('Введите город:')
#         weather = await client.get(city)
#         print(weather.current.temperature, 'градусов в фаренгейт в',city )
#         print('Перевести в цельсии ?')
#         convert = input('Да или Нет')
#         if convert == 'да':
#             Far_Cel = (weather.current.temperature - 32) / 1.8
#             print('В цельсиях, в городе', city, Far_Cel)
#         if convert == 'нет':
#             print('Вот это ты крутой )')
#
#
#
# if __name__ == "__main__":
#     if os.name == "nt":
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.run(getweather())

from colorama import init
from colorama import Fore
import numexpr as num
import pyautogui as py

x = 0
while x == 0:
    print(Fore.LIGHTYELLOW_EX)
    exam = py.prompt("Введите ваш пример", "Математическая операция ")
    res = num.evaluate(exam)
    print(exam, "=", res)
    print(Fore.LIGHTBLUE_EX)
    print("Україна, понад усе!")
    py.alert(res, "Answer", button="Thanks")
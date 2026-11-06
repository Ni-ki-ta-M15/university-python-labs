import random

NAME = [random.randint(-100, 100) for elem in range(10)]
print(f"Массив до: {NAME}")


negative_elements = sorted([i for i in NAME if i < 0], reverse=True)
positive_elements = [i for i in NAME if i >= 0]

NAME = negative_elements + positive_elements
print(f"Массив после: {NAME}")
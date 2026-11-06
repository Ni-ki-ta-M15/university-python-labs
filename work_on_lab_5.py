import random
random_list = [random.randint(0, 100)  for any in range(10)]

random_list.sort()
print(f'First list: {random_list}')


list_of_multiples = []
for any_num in random_list:
    if any_num % 4 == 0:
        list_of_multiples.append(any_num)
print(f'Second list: {list_of_multiples}')


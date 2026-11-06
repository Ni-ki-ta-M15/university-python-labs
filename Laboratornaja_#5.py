import math
# Example 1
birthday = ('15.05.2005')
print('243 group,', 'Малый Никита Михайлович!', birthday)
p_degree = int(input('Enter your degree: '))
n_border = int(input('Enter your border: '))
i = 1

while pow(i, p_degree) <= n_border:
    print(pow(i, p_degree), end='; ')
    i += 1
print(f'\nThe last number in the degree: {i - 1}')

# Example 2

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}", end='  |  ')
#     print("\n\n")

# # TOP Code
# birthday = ('15.05.2005')
# print('243 group,', 'Малый Никита Михайлович!', birthday)
# for i in range(2, 11):
#     for j in range(1, 11):
#         print(f"{i:2d} * {j:2d} = {i*j:3d}", end='  |  ')
#     print("\n\n" + "-" * 178)

# import random
#
# birthday = ('15.05.2005')
# print('243 group,', 'Малый Никита Михайлович!', birthday)
# numbers = [random.randint(1, 100) for _ in range(10)]
#
# print(f'Оригінальний список:{numbers} \n')
# print(f'Відсортований список:{sorted(numbers)}')

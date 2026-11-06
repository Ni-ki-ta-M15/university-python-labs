from colorama import init
from colorama import Fore, Style
init()


print('Any`s array - ')
array = [2, 7, 1, 8, 4, 6, 9, 7, 5, 8, 3, 11, 4, 15, 10]
print(array, end='\n\n')
print(Fore.LIGHTRED_EX,'__________________________________________', Style.RESET_ALL)
list_04 = [array[0],array[1],array[2],array[3],array[4]]
print(Fore.GREEN,'Your 1/3 array - ',list_04)
list_04.sort(reverse=True)
print('Your 1/3 array, but it sort - ', list_04,Fore.LIGHTRED_EX, end='\n\n')
print('__________________________________________')


print(Fore.GREEN)
list_59 = [array[5],array[6],array[7],array[8],array[9]]
print(Fore.GREEN,'Your 2/3 array - ',list_59)
list_59.sort(reverse=True)
print('Your 2/3 array, but it sort - ', list_59,Fore.LIGHTRED_EX, end='\n\n')
print('__________________________________________')


list_1014 = [array[10],array[11],array[12],array[13],array[14]]
print(Fore.GREEN,'Your 3/3 array - ',list_1014)
list_1014.sort(reverse=True)
print('Your 3/3 array, but it sort - ', list_1014,Fore.LIGHTRED_EX, end='\n\n')
print('__________________________________________',Fore.CYAN, end='\n\n', )


sum__array1 = array[0] + array[1] + array[2] + array[3] + array[4]
sum__array2 = array[5] + array[6] + array[7] + array[8] + array[9]
sum__array3 = array[10] + array[11] + array[12] + array[13] + array[14]

print('Your sum 1/3 array - ', sum__array1)
print('Your sum 2/3 array - ', sum__array2)
print('Your sum 3/3 array - ', sum__array3)
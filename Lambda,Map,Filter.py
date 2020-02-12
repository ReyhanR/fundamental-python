# LAMBDA
# biasa digunakan untuk callback function

# ex : 

# lambda num: num * 2

# MAP
# Digunakan untuk merubah bentuk data
# menerima dua input, function dan list
# function yang memiliki istilah callback function
# function ini harus menerima satu buah parameter
# function harus me return sesuatu
# function harus me return sesuatu
# return mapobject, untuk mendapatkan listnya harus dimasukkan kedalam function list()

# ex :

# def times2(num):
#     return num * 2

# numList = [1, 2, 3, 4, 5]

# result = list(map(times2, numList)) # map(function, list)

# print(result)

# # Dengan Lambda

# numList = [1, 2, 3, 4, 5]

# result = list(map(lambda num: num * 2, numList)) # map(function, list)

# print(result)

# FILTER
# Digunakan untuk merubah menyaring data
# menerima dua input, function dan list
# function yang memiliki istilah callback function
# function ini harus menerima satu buah parameter
# function harus me return boolean (True, False)
# return mapobject, untuk mendapatkan listnya harus dimasukkan kedalam function list()

def even(num):
    return num % 2 == 0
    
numList = range(10)

result = list(filter(even, numList)) # with function
result2 = list(filter(lambda x: x % 2 == 0, numList)) # with lambda

print(f'dengan function : {result}')
print(f'dengan lambda : {result2}')

# SEARCH

words = ['sands', 'peace', 'sandals', 'birds', 'dear']





# Soal
# buat sebuah function yang menerima string
# akan menghilangkan semua huruf vokal
# dan me return string yang masuk setelah dihilangkan huruf vokalnya

# Str = 'today is friday and tomorrow is saturday'

# def fltrVokal(x):

#     for i in x:
#         if i not in 'aiueo':
#             return True
    
            
# res = ''.join(filter(fltrVokal, Str))
# print(res)

# numbersEven = [2, 12, 4, 7, 8]
# numbersOdd = [3, 11, 7, 9, 5, 3, 7, 8]

# def outliers(x):
    
#     even = []
#     odds = []

#     for i in x:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odds.append(i)

#     if len(odds) > len(even):
#         return even
#     elif len(even) > len(odds):
#         return odds

# resultEven = outliers(numbersEven)
# resultOdds = outliers(numbersOdd)
# print(resultEven)
# print(resultOdds)

# def get_digits(num, digits = []):
#     while num > 0:
#         digits.append(num % 10)
#         return get_digits(num // 10, digits)
#     if num == 0:
#         return digits


# def multiply_all(digits, multiplier = 1):
#     while len(digits) > 0:
#         multiplier = multiplier * digits.pop(0)
#         return multiply_all(digits, multiplier)
#     if len(digits) == 0:
#         return multiplier


# def persistence(num, count = 0):
#     while num >= 10:
#         num = multiply_all(get_digits(num))
#         count += 1
#         return persistence(num, count)
#     if num < 10:
#         return count

# x = input('Input : ')
# print(persistence(int(x)))

def mult(num):
    
    num = str(num)

    listInt = []

    for i in num:
        listInt.append(int(i))

    count = 0
    while len(listInt) > 1:
        
        res = 1 
    
        for i in listInt:
            res *= i 

        res = str(res)
        listInt = []
        for i in res:
            listInt.append(int(i))

        count += 1

    return count

inputan = int(input('Input Angka : '))
result = mult(inputan)
print(f'Banyaknya perkalian : {result}')



 

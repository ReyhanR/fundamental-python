# Function
# Kumpulan atau blok kode yang dapat diberikan nama dan dapat digunakan secara berulang.
# dapat memiliki input, output dan keduanya.

# # Pembuatan function
# def call():
#     print(f'Hello...')

# # pemanggilan function
# call()

# def gre et(name):
#     print(f'Hello, {name}')

# greet('broh...')

# buat sebuah function yang menerima list
# akan me return hasil kali dua dari semua angka di dalam list

# List = [1, 3, 5, 7]

# def kali(x):
#     y = True
#     while y:
        
# LIST

# menambah elemen list dengan APPEND (menambah selalu diletakkan dipaling belakang)

listAwal = [1, 3, 4, 5]
listAwal.append(7)
print(listAwal)

# menambah elemen list dengan INSERT (menambah dimana saja tergantung index)

listAwal2 = [1, 2, 3, 4, 5]
listAwal2.insert(1, 1) # variabel.insert(index, dataYgInginDiTambah)
print(listAwal2)

# SORT

# Mengurutkan data

listStr = ['Can', 'Angry', 'Evil', 'Forgive']
listInt = [7, 5, 9, 1 ,3]
listBool = [False, True, True, False]

listStr.sort()
print(listStr)

listStr.sort(reverse = True)
print(listStr)

listInt.sort()
print(f'\n{listInt}')

listInt.sort(reverse = True)
print(listInt)

listBool.sort()
print(f'\n{listBool}')

listBool.sort(reverse = True)
print(listBool)
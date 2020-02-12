# DICTIONARY
# Menngunakan kurung kurawal {}
# tidak menggunakan index, melainkan menggunakan property
# penulisan property case-sensitive
# nama property ditulis menggunakan kutip (seperti string)

price = {
    'apple' : 10000,
    'grape' : 15000,
    'orange' : 15000
}

price['grape']

d = {
    'numInt' : 123,
    'numList' : [0, 1, 2],
    'numStr' : 'Hellow',
    'numDict' : { 'insideKey' : 100 }
}

# print(d['numList'])
# print(d['numInt'])
# print(d['numDict'])
# print(d['numDict']['insideKey'])

heroes = {
    'batman' : { 'name' : 'Bruce', 'age' : 41 },
    'ironman' : { 'name' : 'Tony', 'age' : 45 },
    'thor' : {'name' : 'Thor', 'age' : 35 }
}

# print(heroes['ironman'])
# print(heroes['ironman']['age'])

# Function KEYS
# Untuk mendapatkan semua key dari property

# key = heroes.keys()

# for i in key:
#     print(i)

# VALUES
# untuk mendapatkan semua value dari dictionary

values = heroes.values()

# values

# for i in values:
#     print(
#         'Nama : ' + i['name']
#     )

# TUPLE
# Menggunakan kurung ()
# mengenal istilah indexing (dimulai dari nol)
# nilainya tidak dapat dirubah

colorTuple = ('red', 'green', 'blue', 'green', 'blue')

colorTuple [1]
colorTuple [-1]

# code dibawah ini akan error karena nilai tuple tidak dapat dirubah
# colorTuple[0] = 'merah'

# COUNT 
# menghitung banyak data pada tuple

count = colorTuple.count('green')
# print(f'jumlah warna hijau ada : {count}')

# INDEX
# mencari index data tertentu

index = colorTuple.index('blue')
# print(f'warna blue berada pada index : {index}')

persons = (
    {'name' : 'John', 'job' : 'Assassins' },
    {'name' : 'Bruce', 'job' : 'HUnter' },
    {'name' : 'Jajang', 'job' : 'OB' }
)

persons[1]['name'] = 'BruceLee'

print(persons[1])
# Fungsi input digunakan untuk menerima input dari user
#day = input('Masukkan hari : ')
#name = input('Siapa nama anda : ')

#print('Nama anda adalah ' + name)
#print('Hari ini adalah hari ' + day)

# Operator Aritmatik

numOne = 10
numTwo = 5


# Integer menjadi String
# numOneString = str(numOne)
# numTwoString = str(numTwo)


# result = numOne + numTwo
# resultString = str(result)
# print(numOneString + ' + ' + numTwoString + ' = '+ resultString)

# result = numOne - numTwo
# resultString = str(result)
# print(numOneString + ' - ' + numTwoString + ' = '+ resultString)

# result = numOne * numTwo
# resultString = str(result)
# print(numOneString + ' * ' + numTwoString + ' = '+ resultString)

# result = numOne / numTwo
# resultString = str(result)
# print(numOneString + ' / ' + numTwoString + ' = '+ resultString)

# result = numOne % numTwo
# resultString = str(result)
# print(numOneString + ' % ' + numTwoString + ' = '+ resultString)

# result = numOne ** numTwo
# resultString = str(result)
# print(numOneString + ' ** ' + numTwoString + ' = '+ resultString)

# ageJohn = 47
# ageKobe = 41

# # ageJohn = ageJohn + 3
# ageJohn += 3

# # ageKobe = ageKobe - 3
# ageKobe -= 3

# print(str(ageJohn)+' & '+str(ageKobe))

# Module Math
import math

# # Mengabsolute sebuah nilai tanpa mengubah menjadi float
# print(abs(-13))

# # Mengabsolute sebuah nilai kemudian tipe data menjadi float (desimal)
# print(math.fabs(-4))

# # pangkat
# print(math.pow(8,4))

# # Akar Dua
# print(math.sqrt(64))

# # membulatkan bilangan
# print(round(4.7))
# print(round(4.3))

# # Pembulatan Kebawah
# print(math.floor(4.7))

# # Pembulatan Keatas
# print(math.ceil(4.3))

# Operasi STRING

x = 'halo dunia ku yang cerah'

# Menghitung Jumlah karakter pada string
print(len(x))

# Index selalu dimulai dari Nol
print(x.index('dunia'))

# Memisahkan / Split kata berdasarkan karakter tertentu
print(x.split())
print(x.split(' '))

# Mengubah menjadi huruf kecil
print(x.lower())

# Mengubah menjadi huruf besar
print(x.upper())

# Mengubah huruf besar untuk setiap kata
print(x.capitalize())

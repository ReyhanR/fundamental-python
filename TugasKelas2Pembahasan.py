# Ganjil genap
# Genap, habis dibagi 2 atau hasilnya 0 jika di modulus dengan 2 / Ganjil, 

number = int(input('Masukkan angka : '))

if (number % 2 == 0):
    status = 'Genap'
else:
    status = 'Ganjil'

print(f'Angka {number} termasuk bilangan {status}')
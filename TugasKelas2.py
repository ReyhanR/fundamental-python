# Solve It 1

print('Solve It 1')

# Input Variabel (bilangan) dari user
bilangan = int((input('Masukkan bilangan yg akan di cek : ')))

print('')
# Logic Test dan Output
if (bilangan % 2 == 0):
    print(f'Bilangan {bilangan} adalah bilangan Genap')
else:
    print(f'Bilangan {bilangan} adalah bilangan Ganjil')

# Solve It 2

print('')
print('Solve It 2')
print('')
# IMT = massa(kg) / tinggi(meter)^2
# IMT < 18.5 = berat badan kurang
# IMT 18.5 - 24.9 = berat badan ideal
# IMT 25.0 - 29.9 = berat badan berlebih
# IMT 30.0 - 39.9 = berat badan sangat berlebih
# IMT > 39.9 = obesitas

# Input variabel massa dan tinggi dari user
massa = input('Masukkan massa tubuh (Kg) : ')
tinggi = input('Masukkan tinggi badan (Cm) : ')


# Tampilkan info massa dan tinggi user
print(f'Massa Tubuh anda {massa} Kg & Tinggi tubuh anda {tinggi} centimeter')
massa = float(massa)
tinggi = float(tinggi)
print('')

# Hitung IMT user
imt = (massa / ((tinggi / 100)**2))

# Logic Test dan Output IMT
if (imt > 39.9):
    print(f'IMT anda : {imt} (Anda obesitas)')
elif (imt > 30) and (imt < 39.9):
    print(f'IMT anda : {imt} (BB anda sangat berlebihan)')
elif (imt > 25) and (imt < 29.9):
    print(f'IMT anda : {imt} (BB anda berlebih)')
elif (imt > 18.5) and (imt < 39.9):
    print(f'IMT anda : {imt} (BB anda ideal)')
else: 
    print(f'IMT anda : {imt} (BB anda kurang)')


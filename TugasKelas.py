# # SolveIt 1

print('Solve It 1')
# # Input Variabel
x = 4
y = 3
z = 2

# # Proses perhitungan
w = ((x+y*z)/(x*y))**z

# # Output (Hasil)
print(w)

# # SolveIt 2

print('')
print('Solve It 2')
# # Input Variabel
angka = input("Silahkan masukkan angka berapapun : ")

# # Proses Perhitungan 
hasilKuadrat = (int(angka) ** 2) 

# # Output
print("Kuadrat dari "+angka+ " = " + str(hasilKuadrat))

# # Solve It 3

print('')
print('Solve It 3')

hari = 485

tahun = int(hari / 360)
hari = hari % 360

bulan = int(hari / 30)
hari = hari % 30

minggu = int(hari / 7)
hari = hari % 7

print(str(tahun)+ ' Tahun ' +str(bulan)+ ' Bulan ' +str(minggu)+ ' Minggu ' +str(hari) +' Hari ')

# Solve It 4

print('')
print('Solve It 4')
andiBudi = 49
rasioAndi = 2
rasioBudi = 5
totalRasio = rasioAndi+rasioBudi
umurAndiKini = andiBudi/totalRasio*rasioAndi
umurBudiKini = andiBudi/totalRasio*rasioBudi
umurAndi2ThnLg = umurAndiKini + 2
umurBudi2ThnLg = umurBudiKini + 2


print('Umur Andi saat ini : ' +str(umurAndiKini)+ ', 2 tahun lagi menjadi ' +str(umurAndi2ThnLg))
print('Umur Budi saat ini : ' +str(umurBudiKini)+ ', 2 tahun lagi menjadi ' +str(umurBudi2ThnLg))

# Solve It 5

print('')
print('Solve It 5')
x = input('Masukkan kalimat : ')
y = input('Huruf yg ingin diketahui jumlah nya : ')
y = str(y)
x = str(x)

jumlah = x.count(y)

print('Jumlah huruf ' +y+ ' dalam kalimat "' +x+ '" : ' +str(jumlah))

# Solve It 6

print('')
print('Solve It 6')
# Input variabel
jarakMobil = 120
a = 60
b = 40
jamMulai = 9

# Proses penhitungan
waktuTabrak = 120/(a+b)
waktuDlmJam = int(waktuTabrak)
waktuDlmMenit = int((waktuTabrak * 60) % 60)


# Output
print(f'A dan B akan bertabrakan pada {waktuDlmJam} Jam {waktuDlmMenit} Menit ')




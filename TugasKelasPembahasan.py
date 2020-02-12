# Solve It 1

import math
print('Solve It 1')
# Input variabel
x = 4
y = 3
z = 2

# Proses Penghitungan
hasil = (x + y * z) / (x * y)

# Variabel hasil di pangkat z dengan fungsi math.pow
print(math.pow(hasil, z))

# Solve It 2

print('')
print('Solve It 2')
# Meminta input dari user yang disimpan dalam variabel
# Input dari user akan berupa string
numUser = input('Silahkan masukkan sebuah angka : ')

# ubah input dari user menjadi integer
numUser = int(numUser)

# Hitung kuadrat dari input user
result = math.pow(numUser, 2)
result = int(result)

# Output dengan memunculkan di terminal
print(f'Kuadrat dari {numUser} : {result}')

# Solve It 3

print('')
print('Solve It 3')
# 1 tahun = 360 hr , 1 bulan = 30 hr , 1 minggu = 7 hr

# Input jumlah hari dari user (Tentukan banyaknya hari)
daysInputAwal = input('Masukkan jumlah hari : ') 
daysInputSimpan = int(daysInputAwal)

# Tentukan jumlah tahun
tahun = int(daysInputSimpan / 360)
# Sisa hari setelah diambil sekian tahun
daysInputSimpan = daysInputSimpan % 360

# Tentukan jumlah bulan
bulan = int(daysInputSimpan / 30)
# Sisa hari setelah diambil sekian bulan
daysInputSimpan = daysInputSimpan % 30

# Tentukan Jumlah minggu
minggu = int(daysInputSimpan / 7)
# Sisa hari setelah diambil sekian minggu
daysInputSimpan = daysInputSimpan % 7 

# Tentukan jumlah hari
daysAkhir = daysInputSimpan

# Output
print(f'{daysInputAwal} hari sama dengan {tahun} Tahun, {bulan} Bulan, {minggu} Minggu, {daysAkhir} Hari ')

# Solve It 4

print('')
print('Solve It 4')
# Andi + budi = 49
# Rasio = 0.4 = 4/10 = 2/5 = 2 : 5
# Total perbandingan Andi + Budi = 2 + 5 = 7

# Variabel
totalUmur = 49
rasioAndi = 2 
rasioBudi = 5
totalRasio = rasioAndi + rasioBudi

# Cari tahu umur Andi, ditambah 2
umurAndi = totalUmur * (rasioAndi / totalRasio) + 2
umurAndi = int(umurAndi)

# Cari tahu umur Budi, ditambah 2
umurBudi = totalUmur * (rasioBudi / totalRasio) + 2
umurBudi = int(umurBudi)

# Output
print(f'Umur Andi setelah 2 tahun adalah {umurAndi} Tahun')
print(f'Umur Budi setelah 2 tahun adalah {umurBudi} Tahun')

# Solve It 5

print('')
print('Solve It 5')

# Tentukan kalimat awal
text = 'Halo dunia'

# Tentukan karakter yang ingin dicari
find = 'a'

# Cari banyaknya karakter tersebut pada kalimat
# 'Halo dunia'.count(a)
result = text.count(find)

# Output
#

# Solve It 6

# A = 60 km/h
# B = 40 km/h
# Distance = 120 km
# Waktu yang dibutuhkan untuk bertabrakan atau bertemu ?

speedA = 60
speedB = 40
speedTotal = speedA + speedB
distance = 120

timecrash = distance / speedTotal
timeInHour = int(timecrash)
timeInMinute = int((timecrash * 60) % 60)

print(
    f'Akan bertemu setelah {timeInHour} Jam {timeInMinute} Menit'
)

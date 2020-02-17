###############
## R A N G E ##
###############

# Sebuah function yang akan me return list dari integer
# range menerima 1 parameter wajib dam 2 parameter tidak wajib

# menerima 1 parameter
# parameter tsb digunakan sebagai batas akhir angka
# angka pertama dimulai dari nol

resRange = list(range(11))
print(f' range (5) : {resRange}')

# Menerima 2 parameter
# parameter 1 : nilai awal , parameter 2 : nilai akhir (tidak termasuk)

resRange2 = list(range(2, 11))
print(f' range (2, 11) : {resRange2}')

# Menerima 3 parameter
# parameter 1 : nilai awal , parameter 2 : nilai akhir (tidak termasuk), 
# parameter 3 : step, loncatan setiap nilai (default : 1)

resRange3 = list(range(2, 11, 2))
print(f' range (2, 11, 2) : {resRange3}')

resRange4 = list(range(10, 0, -1))
print(f' range (10, 0, -1) : {resRange4}')

resRange5 = list(range(10, 0, -2))
print(f' range (10, 0, -2) : {resRange5}')
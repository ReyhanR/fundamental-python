# TUPLE
# Menggunakan kurung () , akses value menggunakan index

days = ('sunday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday')

# Akses satu value 
days[0] # sunday
days[1] # sunday
days[-1] # friday

# Akses banyak value
days[1:4] # ('monday', 'tuesday', 'wednesday')

# Method Count (menghitung jumlah value tertentu pada tuple)
days.count('sunday') # output = 2 , karena string sunday ada 2 di dalam tuple

# Method Index (mencari index dari suatu value pada tuple)
print(days.index('tuesday')) # output = 3 , tuesday berada pada index ke 3 dalam tuple tersebut

# ... in ... (untuk mengecek apakah suatu value ada didalam tuple, dengan return true/false)
print('saturday' in days) # hasil/return false

# for ... in ... (loop thdp semua data yang ada di dalam list/tuple)
for i in days:
    print(f'Today is {i}')



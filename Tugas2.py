# Harga satuan buah apel 10.000 , anggur 15.000 , jeruk 20.000
# Stock buah apel 5 , anggur 7 , jeruk 8

# Jenis Buah
jenisBuah = ['Apel', 'Anggur', 'Jeruk']

# Stok Buah
stockBuah = [5, 7, 8]

# Harga Buah
hargaBuah = [10000, 15000, 20000]

qty = [0, 0, 0]

# Menu Utama
# Melihat list buah (nama, stok, price)
# Menambahkan list buah
# Belanja Buah

menuUtama = input(
    'Menu Utama\n'+
    '1. Tampilkan list\n'+
    '2. Menambah buah\n'+
    '3. Belanja\n'+
    'Menu pilihan : '
)

if menuUtama == 1:
    print('Create List')
elif menuUtama == 2:
    print('Add list')
elif menuUtama == 3:
    print('Shopping')
        
# Input jumlah buah dari user (Meminta kuantitas dari setiap buah)
# Cek input apakah melebihi kuantitas (stock) (ketika melebihi stock muncul masukkan ulang pesanan)
    for i in range(len(jenisBuah)):
        qty[i] = int(input(f'|Masukkan jumlah pesanan {jenisbuah[i]} : '))
        while (inputApel > stockApel):
            inputApel = int(input(f'Stok Apel kurang (Stok tersedia {stockApel} ), masukkan kembali jumlah pesanan Apel : ')) 
            if (inputApel <= stockApel):
                break
    
# print('')    
# inputAnggur = int(input('|Masukkan jumlah pesanan Anggur : '))    
# while (inputAnggur > stockAnggur):
#     inputAnggur = int(input(f'Stok anggur kurang (Stok tersedia {stockAnggur}), masukkan kembali jumlah pesanan Anggur : '))
#     if (inputAnggur <= stockAnggur):
#         break

# print('')
# inputJeruk = int(input('|Masukkan jumlah pesanan Jeruk : '))
# while (inputJeruk > stockJeruk):
#     inputJeruk = int(input(f'Stok jeruk kurang, (Stok tersedia {stockJeruk}) masukkan kembali jumlah pesanan Jeruk : '))
#     if (inputJeruk <= stockJeruk):    
#         break

# inputApel = inputApel
# inputAnggur = inputAnggur
# inputJeruk = inputJeruk

# # Hitung harga pembelian buah dengan kuantitas, kemudian jumlah harga seluruhnya
# totalHargaApel = (inputApel * hargaApel)
# totalHargaAnggur = (inputAnggur * hargaAnggur)
# totalHargaJeruk = (inputJeruk * hargaJeruk)

# totalHargaSeluruh = (totalHargaApel + totalHargaAnggur + totalHargaJeruk)

# # Tampilkan informasi detail belanjaan
# print('')
# print('===========================')
# print('DETAIL TOTAL BELANJAAN ANDA')
# print('=========================== \n')
# print(f'Jumlah apel {inputApel} X Rp {hargaApel} = Rp {totalHargaApel} \n')
# print(f'Jumlah anggur {inputAnggur} X Rp {hargaAnggur} = Rp {totalHargaAnggur} \n')
# print(f'Jumlah jeruk {inputJeruk} X Rp {hargaJeruk} = Rp {totalHargaJeruk} \n')
# print('')
# print(f'Total Seluruh Belanjaan Anda = Rp {totalHargaSeluruh}')


# bayar = int(input('|Masukkan jumlah uang pembayaran anda : Rp '))
# print('')
# while True:
#     if (bayar < totalHargaSeluruh):
#         selisih = totalHargaSeluruh - bayar
#         bayar = int(input(f'Uang anda ({bayar}) kurang dari harga ({totalHargaSeluruh}), kurang Rp {selisih} | Masukkan uang kembali : Rp '))
#     elif (bayar == totalHargaSeluruh):
#         print('\nTerima kasih, uang anda pas')
#         break
#     elif (bayar > totalHargaSeluruh):
#         kembalian = bayar - totalHargaSeluruh
#         print(f'\nUang anda berlebih anda memiliki kembali sebesar Rp {kembalian}... Terima Kasih')
#         break

        
    
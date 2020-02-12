 # z = ''
# for item in range(5):
#    for item1 in range(5, item, -1):
#       z += ' * '
#    z += '\n'
# for item2 in range(5):
#    for item3 in range(item2 + 1):
#       z += ' * '
#    z += '\n'
# for item in range(5):
#    for item1 in range(5, item, -1):
#       z += ' * '
#    z += '\n'
# print(z);

# totalHargaSeluruh = 2000
# bayar = int(input('|Masukkan jumlah uang pembayaran anda : Rp '))
# while True:
#     if (bayar < totalHargaSeluruh):
#         bayar = int(input(f'Uang anda ({bayar}) kurang dari harga ({totalHargaSeluruh}) | Masukkan uang kembali : Rp '))
#     elif (bayar == totalHargaSeluruh):
#         print('Terima kasih, uang anda pas')
#         break
#     elif (bayar > totalHargaSeluruh):
#         kembalian = bayar - totalHargaSeluruh
#         print(f'Uang anda berlebih anda memiliki kembalian sebesar Rp {kembalian}... Terima Kasih')
#         break

# while True:
#     if (bayar < totalHargaSeluruh):
#         selisih = totalHargaSeluruh - bayar
#         bayar = int(input(f'Uang anda ({bayar}) kurang dari harga ({totalHargaSeluruh}) selisih ({selisih}) | Masukkan kekurangan : Rp '))
#         bayarSisa = bayar
#         if (bayar > selisih):
#             print('Berlebih...')
#         elif (bayar < selisih):
#             bayar = bayarSisa + selisih
#             bayar = int(input(f'Uang anda ({bayar}) kurang dari harga ({totalHargaSeluruh}) selisih ({selisih}) | Masukkan kekurangan : Rp '))
#             # print('kekurangan...')
#         else:
#             break
#     elif (bayar == totalHargaSeluruh):
#         print('Terima kasih, uang anda pas')
#         break
#     elif (bayar > totalHargaSeluruh):
#         kembalian = bayar - totalHargaSeluruh
#         print(f'Uang anda berlebih anda memiliki kembalian sebesar Rp {kembalian}... Terima Kasih')
#         break

def tambah(objek):
    print(f'Kata {objek}')
        
stockApple = 5
stockGrape = 7
stockOrange = 8

priceApple = 10000
priceGrape = 15000
priceOrange = 20000

qtyApple = int(input('Masukkan jumlah Apel : '))
if (qtyApple > stockApple):
    print(f'Kesalahan input, stock Apel = {stockApple}')
    qtyApple = 0
    
qtyApple = int(input('Masukkan jumlah Anggur : '))
if (qtyGrape > stockGrape):
    print(f'Kesalahan input, stock Anggur = {stockGrape}')
    qtyGrape = 0

qtyApple = int(input('Masukkan jumlah Jeruk : ')) 
if (qtyOrange > stockOrange):
    print(f'Kesalahan input, stock Jeruk = {stockOrange}')
    qtyOrange = 0

totalApple = qtyApple * priceApple
totalGrape = qtyGrape * priceGrape
totalOrange = qtyOrange * priceOrange

totalPrice = totalApple + totalGrape + totalOrange

Print(
    'Detail Belanja \n\n' +
    f'Apel : {qtyApple} X {priceApple} = {totalApple} \n'+
    f'Apel : {qtyGrape} X {priceGrape} = {totalGrape} \n'+
    f'Apel : {qtyOrange} X {priceOrange} = {totalOrange} \n'+
    f'Total = {totalPrice}'
    )


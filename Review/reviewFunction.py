# Function a/ blok kode yang memiliki nama dan dapat di running secara berulang
# sebuah function, dapat memiliki :
# Input atau Output , atau keduanya
# Sebuah function dapat 'menghasilkan' nilai

#####################################
## Function tanpa input dan output ##
#####################################

# Deklarasi / pembuatan function
def pure():
    resSum = 4 + 7
    print(f'Hasil penjumlahan : {resSum}')

# Running function, nama function diikuti dengan kurung ()
pure()

###############################
## Function dgn sebuah input ##
###############################
# byknya jumlah input tidak terbatas
def whatday(day, feel):
    day = day.capitalize()

    print(f'Today is {day} , and i\'m {feel}')

whatday('sunDAy', 'happy')
whatday('SUNDAY', 'sad')
whatday('sunday', 'bored')

##################################
## Function dengan sebuah ouput ##
##################################

# mengeluarkan / output value dengan menggunakan return

def Sum(x, y):
    res = x + y
    return res

    print('Not running') # kode ini tidak akan running , karena setelah return kode tidak akan di running

inputX = int(input('Input angka 1 : '))
inputY = int(input('Input angka 2 : '))

resSum = Sum(inputX, inputY)
print(f'Hasil : {resSum}')

    



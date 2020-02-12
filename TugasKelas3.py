
InputJmlElemenList = []
InputJmlElemenList = int(input('Masukkan elemen array : '))
listAcak = []

for i in range (0, InputJmlElemenList):
        listAcak.append(int(input('Masukkkan Element list : ')))

def minMax(listNumber):

    order = []
    lowest = []

    for i in listNumber:
        if listNumber[i] < 0:
            lowest = listNumber[i]
        i += 1
        if i == len(listNumber):
            order.append(lowest)
            listNumber.append(lowest)
            if listNumber:
                lowest = listNumber
            i = 0

    high = order[-1]    

    return (order, lowest, high)
           
minMax(listAcak)
        




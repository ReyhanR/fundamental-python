# Pertama
# Cara pertama
# listInput = []

# element = int(input('Masukkan jumlah element list : '))

# for i in range (0, element):
#     ele = int(input('Masukkkan Element list : '))
#     listInput.append(ele)
    

# listOne = listInput

# def multiTwo(data):
    
#     listFinal = []

#     for i in data:
#         res = i * 2
#         listFinal.append(res)
    
#     return listFinal

# finalResult = multiTwo(listOne)
# print(f'\nHasil X 2 nya adalah : {finalResult}')

# # Cara kedua
# listOne = listInput

# def multiTwo(data):
    
#     listFinal = [i * 2 for i in data]    
#     return listFinal

# finalResult = multiTwo(listOne)
# print(f'\nHasil X 2 nya adalah : {finalResult}')

# KEDUA

startList = [23, 43, 56, 32, 67, 54, 87, 59]

def oddEven(listNumber):

    oddList = []
    evenList = []
    finalList = []

    for i in listNumber:
        if i % 2 == 0:
            # input ke array genap
            evenList.append(i)
        else:
            # input ke array ganjil
            oddList.append(i)    

    finalList.append(evenList)
    finalList.append(oddList)

    return finalList

result = oddEven(startList)
print(result)    

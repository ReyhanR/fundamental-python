listInput = []

element = int(input('Masukkan jumlah element list : '))

for i in range (0, element):
    ele = int(input('Masukkkan Element list : '))
    listInput.append(ele)


def funList(data):
    for x in data:
        [data[i] * [data[i + 1]] for i in range(len(data)-1)]
    return data


res = funList(listInput)
print(res)    


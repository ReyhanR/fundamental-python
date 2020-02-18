listInput = []
listTrash = []
listGenap = []
listGanjil = []

y = 1
print('Input sampai 7 angka (kombinasi ganjil dan genap)')
while len(listInput) <= 6:
    ele = int(input(f'Masukkkan Element ke-{y} : '))
    if ele <= 9:
        listInput.append(ele)
        y += 1
    if ele >= 9:
        listTrash.append(ele)

for i in listInput:
    if i % 2 == 0:
        listGenap.append(i)    
    else:
        listGanjil.append(i)

def average(z):
    return sum(z)/len(z)

avRes = average(listGanjil)

print(f'Angka yang terinput : {listInput}')
listInput.sort()
print(f'Sort ascending : {listInput}')
listInput.sort(reverse=True)
print(f'Sort descending : {listInput}')
print(f'Hasil jumlah angka genap : ', sum(listGenap))
print(f'Hasil rata rata angka ganjil : {avRes}')

 
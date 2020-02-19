import numpy as np 
n=int(input("Jumlah baris dalam list : "))
arr=[]
print("Input elemen (dipisahkan dengan koma): ")
for i in range(n):
    l=list(map(int,input().split(",")))
    arr.append(l)
print("List yang di input :")
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
m=np.array(arr,int)
s=input("kiri/kanan:")
d=input("Berapa Kali :")
degrees={"1":1,"2":2,"3":3}
if(s=="kiri" or s=="Kiri" or s=="kIRI"):
    m=np.rot90(m,degrees[d])
else:
    m=np.rot90(m,4-degrees[d])
print("The Matrix after rotation by the given degree.")
for i in range(n):
    for j in range(n):
        print(m[i][j],end=' ')
    print()
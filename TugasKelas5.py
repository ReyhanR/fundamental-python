# def wordRev(word):

#     wordSplit = word.split()
#     Str = []

#     for i in wordSplit:
#         for z in i:
#             Str = z + Str
        
#     print(Str)

# wordRev('Hello My Friend')

def sum01(lis):
    noIndexNol = lis.index(0)
    noIndexSatu = lis.index(1) + 1

    del lis[noIndexNol:noIndexSatu]

    result = sum (lis)

    return result

res = sum01([7, 0, 3, 1, 7, 9])
print(res)

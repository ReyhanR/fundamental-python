# strList = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']

# inputUser = input(f'List {strList}\nSearch : ')

# def srch(x):
#     return inputUser.lower() in x.lower()

# result = list(filter(srch, strList))

# print(f'\nHasil : {result}')

# numList = [1, 2, 3, 4, 5]

# def times2(num):
#     return num * 2

# def myMap(fun, lis):
#     mapList = []
#     for i in lis:
#         res = fun(i)
#         mapList.append(res)
#     return mapList

# result = myMap(times2, numList)
# print(result)

# strList = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam', 'Anto']

# inputUser = input('Search : ')

# def fltr(x):
#     return inputUser.lower() in x.lower()
        
# def myFilter(fun, lis):
#     filterList = []
#     for i in lis:
#         if fun(i) == True:
#             filterList.append(i)
#     return filterList     

# result = myFilter(fltr, strList)
# print(f'Hasil : {result}')

# for in , if else , len(), join, print()

# employee = [
#     {"name" : 'Steve', "gender" : 'male', "hobbies" : ['video games', 'football']},
#     {"name" : 'lina', "gender" : 'female', "hobbies" : ['shop', 'cook']},
#     {"name" : 'Reynald', "gender" : 'male', "hobbies" : ['run', 'hide', 'jump']}
# ]

# # output = Mr. Steve has 2 hobbies, they are video games, football

# for i in employee:
#     if i["gender"] == 'male':
#         i["name"] = 'Mr. ' + i["name"]
#     else:
#         i["name"] = 'Mrs. ' + i["name"]
     
#     z = ', '
#     print(f'{i["name"]} has {len(i["hobbies"])} hobbies, they are {z.join(i["hobbies"])}\n')

# inputUser = input('Input kata : ')

# def changeWord(x):
#     vocal = ['a', 'i', 'u', 'e', 'o']
#     if x[0] in vocal:
#         x = x + 'yay'
#     else:
#         x = x[1:] + x[0] + 'ay'
        
#     return x

# res = changeWord(inputUser)
# print(res)

# List = ['a', 'b', 'c']
# List.reverse()
# print(List)

# inputUser = input('Sentence : ')
# def sentenceRev(word):

#     wordSplit = word.split()

#     wordSplit.reverse()

#     wordJoin = " ".join(wordSplit)

#     print(wordJoin)
   
# sentenceRev(inputUser)

# Has 99


def has99(lis):
    noIndex = lis.index(9)
    return lis[noIndex + 1] == 9

print(has99([1, 9, 9]))
print(has99([5, 9, 2, 9]))
print(has99([9, 3, 9]))
print(has99([7, 9, 9, 6]))


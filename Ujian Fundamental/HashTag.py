Lis = 'how are you doing'

def hashtag(x):

    newLis = list(x)

    newList = []


    if len(newLis) <= 20:

        for i in newLis:

            if i == newLis[0]:
            
                newList.append('#')
                newList.append(i)
            else:
                newList.append(i)
    else :
        print(False)

    newStr = ''.join(newList)
    StrwSpaces = newStr.replace(' ', '')

    print(StrwSpaces)

hashtag(Lis)

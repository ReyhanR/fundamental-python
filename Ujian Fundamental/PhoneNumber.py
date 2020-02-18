
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# def phoneNumber(lisNum):

#     frontLis = []
#     CentLis = []
#     lastLis = []

#     while len(lisNum) == 9:

#         frontLis.insert(0, '(')
#         frontLis.insert(lisNum[0:3]
#     else:

#         return False
        

        
                
    

# res = phoneNumber(number)
# print(res)

##################                
# jawaban hilman #
##################

def pnumber(x) :
    res = len(x)
    if res >9 :
        phoneList = []
        for num in x:
            phoneList.append("". join(str(num)))
        phStr = phoneList
        print(phoneList)
        ac = "".join(phStr[0:3])
        prefix = "".join(phStr[3:6])
        suffix = "".join(phStr[6:10]) 
        print("({}) {}-{}".format(ac, prefix, suffix))
    else :
        print("False")
    
pnumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
pnumber([1, 2, 3, 4, 5, 6, 7, 8, 9])
            



         


def taban(a,t):
    sonuc=0
    basamak=1
    while(a>0):
        sonuc =sonuc +(int(a%t)*basamak)
        basamak = basamak*10
        a = a/t
    return sonuc

def intToList(val):
    d = []
    c=str(val)
    for digit in c:
        d.append(int(digit)-1)
    return d

def uniqList(listt):
    for i in range(len(listt)):
        val=listt[i]
        for x in range(i+1,len(listt)):
            if val==listt[x]:
                return False

    return True


def allPermList(m,n):

    #m = m-n
    #m+=1
    #n=3
    #m=3#5
    digit=1
    diz=0
    for i in range(n):
        diz=diz+digit
        digit = digit*10
    kat = diz
    diz=0
    tValue = 0
    allList = []
    for x in range(pow(m,n)-1):
        diz = diz+1
        tValue = kat + taban(diz,m)
        listValue=intToList(tValue)
        if uniqList(listValue)==True:
            allList.append(listValue)
            #print(listValue)
    return allList

inputTable = [[5,8,7],
              [8,12,7],
              [4,8,5]]

def findValue(list1,table):
    res=0
    for k in range(len(list1)):
        res = res + table[k][list1[k]]
    return res

def findOptimalAssistantship(inpTable):
    x=len(inpTable)
    z=len(inpTable[0])
    if x != z:
        print("Öğretmen Sayısının fazla olduğu durumu handle etmedim, sadece kare matriste çalışıyorum.")
        return 0,0
    arrays=allPermList(x,z)
    min=findValue(arrays[0],inpTable)
    tmin=0
    returnList =[]
    tempList = []
    for i in range(len(arrays)):
        tempList = arrays[i]
        tmin=findValue(tempList,inpTable)
        if tmin<=min:
            returnList = tempList
            min=tmin
    #print(returnList,"# RA0,...")
    return returnList,min


a = []
b = 0
a,b = findOptimalAssistantship(inputTable)

print(a)
print(b)
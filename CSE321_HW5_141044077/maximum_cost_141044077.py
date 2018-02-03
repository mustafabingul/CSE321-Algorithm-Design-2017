"""
gelen inputu 3 erli elemanları halinde 3 durumada 1
getirildiğinde maximum maliyeti en iyisi hangisi ise öyle
yerleştirip devam ettim. Önceki maximum değerlerini arraylerde
depolayıp daha sonra nereye 1 konulsa daha iyi maliyet elde ederimi
kontrol edip devam ettim.

worst-case analysis:
asıl fonksiyonum n kez dönmekte,
onun içinde çağırdığım 2 helper fonksiyon var, biri n kez dönerken
diğeri ise constant zamanda çalışmakta.
sonuç olarak; genel algoritma O(n^2) karmaşıklığına sahip.
"""

def helperS(arr):
    n=len(arr)
    a=0
    sum=0
    for i in range(1,len(arr)):
        sum+=abs(arr[i]-arr[i-1])
    return sum

def helperF(array):
    s0=0
    s1=0
    f0Back=array.copy()
    f1Back = array.copy()
    r0Back=[]
    r1Back=[]
    f0Back[0]=1
    f0Back[2]=1
    r0Back=f0Back
    f1Back[1]=1
    r1Back=f1Back
    s0=helperS(r0Back)
    s1=helperS(r1Back)
    #print("CC")
    if(s0>s1):
        #print("CC1")
        return r0Back
    else:
        #print("CC2")
        return r1Back

def find_maximum_cost(rArray):
    bUp=rArray.copy()
    costArray=[]
    cost=0
    for k in range(len(rArray)-2):
        bUp[k:k+3]=helperF(bUp[k:k+3])
    cost=helperS(bUp)
    return cost



aa=[14,1,14,1,14]
aaa=[1,9,11,7,3]
aaaa=[50,28,1,1,13,7]

c=find_maximum_cost(aa)
print(c)




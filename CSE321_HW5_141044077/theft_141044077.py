
"""
referans:
buradaki örnekten yola çıkarak çözmeye çalıştım hocam.
https://www.youtube.com/watch?v=lBRtnuxg-gU

verilen iki boyutlu arrayin sol tarafından sağına doğru
sürekli gidebileceği yerleri sağ yukarı sağa ve sağ aşağı
olmak üzere sürekli maximumu önceki ile toplayarak sağa doğru ilerledim.

worst-case analaysis: O(n^2) karmaşıklığına sahiptir.
"""
def fo(ar,ind):
    a=[]
    if ind==0:
        a.append(ar[ind])
        a.append(ar[ind+1])
        return max(a)
    if ind+1==len(ar):
        a.append(ar[ind])
        a.append(ar[ind-1])
        return max(a)
    else:
        a.append(ar[ind])
        a.append(ar[ind+1])
        a.append(ar[ind-1])
        return max(a)
def theft(array):
    #a = [[0]*len(array)]*len(array)
    newA = []
    b=[]
    c=[]
    c=0
    sm=0
    for l in range(len(array)):
        for m in range(len(array)):
            b.append(array[m][l])
    for i in range(len(array)):
        newA.append([])
        for j in range(len(array)):
            newA[i].append(b[c])
            c+=1
    o=max(newA[0])
    #print(o,"A1")
    #print(newA[0])
    p=newA[0].index(max(newA[0]))
    #print(p,"PP")
    sm=o
    for u in range(1,len(array)):
        x0=fo(newA[u],p)
        sm+=x0
        #print(x0,"KK")
        p=newA[u].index(x0)
    return sm

i2=[[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]

aA=theft(i2)
print(aA)

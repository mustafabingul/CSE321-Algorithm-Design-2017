

"""

avantajları:
hoare partition daha etkilidir lomuto partitiondan.
hoare partition arrayin başından ve sonundan olmakla birlikte
iki tane index ile çalışır.
lomuto partitionu implement etmek daha kolay ve basittir.

dezavantajları:
eğer gelen input arraylar sıralıya yakın arraylar ise,
hoare partititon neredeyse hiç swap yapmazken, lomuto partition
array size ının yarısına yakın swap yapar.


"""
def hoare0(array0,l0,h0):
    pivot=array0[l0]
    a=l0-1
    b=h0+1

    while(1):
        while(1):
            a=a+1
            if not(array0[a]<pivot):
                break
        while(1):
            b=b-1
            if not(array0[b]>pivot):
                break
        if(a>=b):
            return b
        t=array0[b]
        array0[b]=array0[a]
        array0[a]=t
def hoare1(array1,l1,h1):
    if(l1<h1):
        c=hoare0(array1,l1,h1)
        hoare1(array1,l1,c)
        hoare1(array1,c+1,h1)

def quickSortHoare(array):
    hoare1(array,0,len(array)-1)
    return array

def lomuto1(array1,l1,h1):
    pivot = array1[h1]
    s = l1-1
    for x in range(l1,h1):
        #print(x, "XX")
        if (array1[x] <= pivot):
            s += 1
            tmp = array1[x]
            array1[x] = array1[s]
            array1[s] = tmp

    t = array1[s+1]
    array1[s+1] = array1[h1]
    array1[h1] = t
    return s+1

def lomuto0(array0,l0,h0):
    if(l0<h0):
        c=lomuto1(array0,l0,h0)
        lomuto0(array0,l0,c-1)
        lomuto0(array0,c+1,h0)

def quickSortLomuto(array):
    lomuto0(array,0,len(array)-1)
    return array



arr = [15,4,68,24,75,16,42]
arr2 = [9,5,2,3,10,1,4,2]

print(arr)
print(arr2)
aa=quickSortLomuto(arr)
print(aa)
bb=quickSortHoare(arr2)
print(bb)

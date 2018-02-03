
def compareScales (leftScaleList, rightScaleList):
    result = sum(leftScaleList) - sum(rightScaleList)
    if result < 0:
        return 1
    elif result > 0:
        return -1
    else:
        return 0


def searchIndex(arrayy,a,b):
    mid = (int)((b + a) / 2)

    if (b-a)%2==0:

        if (arrayy[a:mid]==arrayy[mid:b]):
            return -1
        if (b - a == 2):
            if (arrayy[a] > arrayy[b - 1]):
                return b-1
            elif (arrayy[a] < arrayy[b - 1]):
                return a

        if compareScales(arrayy[a:mid],arrayy[mid:b])==1:
           return searchIndex(arrayy,a,mid)
        elif compareScales(arrayy[a:mid],arrayy[mid:b])==-1:
           return searchIndex(arrayy,mid,b)
        else:
            return mid


    elif (b-a)%2!=0:

        if (arrayy[a:mid+1]==arrayy[mid:b]):
            return -1

        if compareScales(arrayy[a:mid+1], arrayy[mid:b]) == 1:
           return searchIndex(arrayy, a, mid)
        elif compareScales(arrayy[a:mid+1], arrayy[mid:b]) == -1:
           return searchIndex(arrayy, mid, b)
        else:
            return (mid)
    else:
        return -2


arr = [1,1,1,1,1,1,1,1,1,1]
arr2 = [1,1,1,1,1,1,1,1,1,0.5]
arr3 = [1,0.5,1,1,1,1,1]
arr4 = [0.5,1,1,1,1,1,1,1,1]


print(searchIndex(arr,0,len(arr)))
print(searchIndex(arr2,0,len(arr2)))
print(searchIndex(arr3,0,len(arr3)))
print(searchIndex(arr4,0,len(arr4)))



"""

Divide and conquer algortiması değil.
complexity analysis: O(n)

yaptığınız açıklamayı gördüğümde herşey için çok geç ti hocam.

"""

def findSub(array,n):
    resultArray1 =[]
    resultArray2 =[]
    min1=100000
    min0=100000
    resAr=[]
    for k in range(n):
        if(min1>0):
            min1=array[k]
            resultArray1.append(array[k])
        else:
            resultArray2.append(array[k])
            min1 += array[k]
        min0=min(min0,min1)
    a=array.index(min(resultArray1))
    #print(a,"AA")
    b=array.index(min(resultArray2))
    #print(b,"BB")
    for n in range(a,b+1):
        resAr.append(array[n])
        #print(array[n],"NN")
    #print(resultArray1)
    #print(resultArray2)
    return resAr

def min_subarray_finder(_array):
    res=findSub(_array,len(_array))
    return res

inpArr = [1,-4,-7,5,-13,9,23,-1]
inp=[1,1,-1,5,1,5,-2,-2,1,-10]
print(min_subarray_finder(inpArr))
print(min_subarray_finder(inp))

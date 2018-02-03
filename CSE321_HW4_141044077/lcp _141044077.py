
"""

explanation:
verilen string arrayini ikiye bölerek yapıyorum,
en son iki eleman kaldığında yazdığım helper fonksiyonda
postfix durumlarını kontrol ediyorum.

worst-case complexity analysis:
en kötü durumu n tane string vardır elimizde
ve hepsi birbiri ile aynıdır.
her string uzunluğuna da k dersek.
en kötü durumda; O(k*n) olacaktır.

"""
def helperCommonPostfixFunc(source, destination):
    s = len(source)
    d = len(destination)
    # print(s,d)
    # print("source---->",source,"destination---->",destination)
    common = ""
    i = s - 1
    j = d - 1
    if (i == 0 or j == 0 or i == -1 or j == -1):
        # print("AGG<<--",i,j)
        return common
    # print("I< ",i,"J< ",j)
    while ((i >= 0) and (j >= 0)):
        # print(source[i])
        if (source[i] != destination[j]):
            break
        common += source[i]
        i -= 1
        j -= 1
    common = common[::-1]
    # print("common",common)
    return common

def helperCommonPostfixFuncTwo(array, firstSize, lastSize):
    s1 = ''
    s2 = ''
    # print(lastSize,firstSize)
    if (firstSize == lastSize):
        return array[firstSize]
    if (lastSize > firstSize):
        midSize = int((firstSize + lastSize) / 2)
        # print("MID",midSize,"FİRST",firstSize,"LAST",lastSize)
        s1 = helperCommonPostfixFuncTwo(array, firstSize, midSize)
        s2 = helperCommonPostfixFuncTwo(array, midSize + 1, lastSize)
        # print("S",s1,"SS",s2)
        return helperCommonPostfixFunc(s1, s2)

def longest_common_postfix(stringList):
    n = len(stringList)
    res = ''
    res = helperCommonPostfixFuncTwo(stringList,0,n-1)
    # print(res,"RES")
    #print(res)
    return res



inpStrings = ["absorptivity",
              "circularity",
              "electricity",
              "importunity",
              "humanity"]

inp2=["mustafa","mustafa","mustafa","mustafa","mustafa",]
inp =["common","kammon","kimtmon"]


print(longest_common_postfix(inpStrings))
print(longest_common_postfix(inp))


mapOfGTU2 = {1 : set([2,3]),
             2 : set([1,3,4]),
             3 : set([1,2,4]),
             4 : set([3,2]),
             5 : set([6]),
             6 : set([5])}

mapOfGTU1 = {1 : set([2,3]),
            2 : set([1,3]),
            3 : set([1,2])}
mapOfGTU3 = {1 : set([]),
             2 : set([]),
             3 : set([]),
             4 : set([]),
             5 : set([]),
             6 : set([])}

def gtuBFS(GTUgraph,root):
    visited = set()
    queue = [root]
    while queue:
        GTUlab = queue.pop(0)
        if GTUlab not in visited:
            visited.add(GTUlab)
            queue.extend(GTUgraph[GTUlab]-visited)
    return visited

def findMinimumCostToLabifyGTU(l,r,graphGTU):

    if l<r:
        return len(graphGTU)*l
    minCost=0
    labCount=0
    roadCount=0
    all=set()
    lst = []
    for i in range(1,len(graphGTU)+1):
        s=gtuBFS(graphGTU,i)
        all.add(tuple(s))
    labCount = len(all)
    lst = list(all)
    for j in range(len(lst)):
        roadCount = roadCount + (len(lst[j])-1)
    minCost = l*labCount + r*roadCount
    return minCost

a = findMinimumCostToLabifyGTU(1,2,mapOfGTU1)
print("Minimum-cost",a)
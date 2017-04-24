

def union(a,b):
    totes = [i for i in a] + ([i for i in b if not i in a])
    #print totes
    return totes

def intersection(a,b):
    totes = [i for i in a if i in b]
    #print totes
    return totes

def setDifference(a,b):
    totes = [i for i in a if i not in b]
    #print totes
    return totes
    

def SymmetricDifference(a,b):
    u = union(a,b)
    i = intersection(a,b)
    totes = setDifference(u, i)
    #print totes
    return totes

def cartesian(a,b):
    totes = [(a[i],b[i]) for i in range(len(a))]
    totes += ([(a[i],b[len(a)-1-i]) for i in range(len(a))])
    #print totes
    return totes

print("testing union of [1,2,3], [4,5,6]:")
print(union([1,2,3], [4,5,6]))

print("testing intersection of [1,2,3], [2,3,4]:")
print(intersection([1,2,3], [2,3,4]))

print("testing set difference of [1,2,3], [2,3,4]:")
print(setDifference([1,2,3], [2,3,4]))

print("testing symetric differnce of [1,2,3], [2,3,4]:")
print(SymmetricDifference([1,2,3], [2,3,4]))

print("testing Cartesian of [1,2], [red, white]:")
print(cartesian([1,2], ["red", "white"]))

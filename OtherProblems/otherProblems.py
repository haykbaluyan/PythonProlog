#extractSlice([5,6,7,8,9,10,11,12],2,5)==[7,8,9]
from random import randrange
from itertools import permutations
def extractSlice(L,begin,end):
    return L[begin:end]
#rotateLeft([a,b,c,d,e],3)==[d,e,a,b,c]
def rotateLeft(L,N):    #this does not change initial list L
    result=L[N:]
    result.extend(L[:N])
    return result
def rotateLeftMod(L,N):    #this modifies initial list L
    for iter in range(N):
        L.append(L.pop(0))
    return L
def removeKthElem(L,K):
    if K>=len(L):
        return []
    L.pop(K)
    return L
def insertGivenPos(L,K,d):
    L.insert(K,d)
    return L
def randomElems(L,k):
    for i in range(len(L)-k):
        i=randrange(len(L))
        L.pop(i)
    return L
def randomElemsFromRange(M,k):
    Y=[]
    L=list(range(M))
    for i in range(k):
        i=randrange(len(L))
        Y.append(L[i])
        L.pop(i)
    return Y
def generateRandomPerm(L):
    allPerms=list(permutations(L))
    index=randrange(len(allPerms))
    return list(allPerms[index])

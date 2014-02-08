##duplicate elements of the list
##ex. duplElems([1,2,3])==[1,1,2,2,3,3]
def duplElems(L):
    #for empty list return empty list
    if len(L)==0:
        return []
    for iter in range(0,2*len(L),2):
        L.insert(iter,L[iter])
    return L
    

##slice list into 2 parts
##ex. sliceList([1,2,3,4,5],2)==[[1,2],[3,4,5]]

def sliceList(L,N):
    if N>len(L):
        return []
    L1=L[0:N]
    L2=L[N:]
    return [L1,L2]
    

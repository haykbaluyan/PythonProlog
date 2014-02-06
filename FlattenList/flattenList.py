#complexity O(n+k) where n is number of total elements, k is number of nested lists
#[[1,2],[3,4],5] -> n=5, k=2;;
def flattenList(X):
    Y=[];
    for item in X:
        if type(item) is list:
            Y+=flattenList(item)
        else:
            Y+=[item]
    return Y
def start(L):
    print(flattenList(L))

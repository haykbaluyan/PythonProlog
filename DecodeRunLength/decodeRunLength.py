##this function decodes encoded length list
##decodeRunLength([1,2,[2,4],[5,1],'q'])==[1,2,4,4,1,1,1,1,1,'q']

def decodeRunLength(L):
    #for empty list return empty list
    if len(L)==0:
        return []

    result=[]
    for elem in L:
        if type(elem) is list:
            for iter in range(elem[0]):
                result.append(elem[1])
        else:
            result.append(elem)
    return result

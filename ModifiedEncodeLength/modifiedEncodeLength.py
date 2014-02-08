##modifed encode length
## [1,1,2,1,3,3,3,3,1,1,1] -> [[2,1],2,1,[4,3],[3,1]]

def modEncodeLength(L):
    #for empty L return empty list
    if len(L)==0:
        return []

    #keep current element under consideration
    cur=L[0]
    #keep curretn list under consideration
    curList=[cur];

    result=[]
    #iterate through the list
    for el in L[1:]:
        if el==cur:
            curList.append(el)
        else:
            if len(curList)!=1:
                result.append([len(curList),cur])
            else:
                result.append(cur)
            cur=el
            curList=[el]
    if len(curList)!=1:
            result.append([len(curList),cur])
    else:
            result.append(cur)  
    return result

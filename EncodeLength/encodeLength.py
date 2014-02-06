##length encoding on the list
##Consecutive duplicates of elements are encoded as terms [N,E]
##where N is the number of duplicates of the element E
##example [2,2,2,2,7,2,2,3,3,4,4,4,4,4]->[[4,2],[1,7],[2,2],[2,3],[5,4]]

def encodeLength(L):

    #for empty list return an empty list
    if len(L)==0:
        return []

    #list to keep the result
    resultList=[]
    #keep track on current candidate element
    cur=L[0]
    #keep number of duplicates for current candidate element
    curNumber=1
    
    for item in L[1:]:
        if item==cur:
            curNumber+=1   #found duplicate of the candidate element
        else:
            resultList.append([curNumber,cur])
            curNumber=1
        cur=item
    resultList.append([curNumber,cur])
    return resultList

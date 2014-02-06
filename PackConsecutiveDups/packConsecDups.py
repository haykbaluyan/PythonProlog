##pack consecutive duplicates in a list
##example [1,2,1,1,2,2,2,1,3] -> [[1],[2],[1,1],[2,2,2],[1],[3]]

def packConsecDups(L):
    #for empty list return an empty list 
    if len(L)==0:
        return []
    resultList=[]  #resulting list containing lists of packed consecutive duplicates
    cur=L[0]        #keep track of current element, which need its own list
    listForDups=[cur];  #list to pack each set of consecutive duplicates

    #go through all element of the original list
    #check consective items and insert duplicates in a new list
    for item in L[1:]:      
   
        if cur==item:
            listForDups.append(item)
        else:
            resultList.append(listForDups)
            listForDups=[item]
        
        cur=item
    resultList.append(listForDups)  # append last list of duplcates 
    return resultList
        

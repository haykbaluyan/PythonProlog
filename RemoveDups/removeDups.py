def removeDups(L):
    if len(L)==0:
        return
    cur=L[0]
    Y=[cur];
    for item in L:
        if cur!=item:   
            Y.append(item)
        cur=item
    return Y
            
            

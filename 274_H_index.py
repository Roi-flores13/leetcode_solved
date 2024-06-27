def Hindex(citations):
    H_index = 0
    
    if sorted(citations, reverse=True)[0] == 0:
        return 0
    
    for index, publication in enumerate(sorted(citations, reverse=True)):
        
        if publication >= index + 1:
            H_index = index + 1
        else:
            return H_index
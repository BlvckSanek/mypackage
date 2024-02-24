def top_n(items, n):
    """
    Return the top n items in an array, is desc order
    
    Args:
        items (array): list or array-like object
        n (int): number of items to return
        
    Return:
        array: top n items, in desc order
    """
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[i]:  # if this item is bigger than the next items
                items[j], items[i] = items[i], items[j] # swap the two
    
    # get last two items        
    top_n = items[-n:]
    
    # return in descending order
    return top_n[::-1]
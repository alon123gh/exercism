
def bin_search(search_list, start, end , value):
    print(start,end)        
    size = end-start
    if size == 0:
         return None
    mid_point = size//2         
    mid = search_list[start+mid_point]    
    if mid == value:
        return start+mid_point
    if value < mid:
        return bin_search(search_list,start, start+mid_point, value )
    if value > mid:
        return bin_search(search_list,start+mid_point+1, end , value )
        
def find(search_list, value):
    search_list.sort()
    index =  bin_search(search_list, 0, len(search_list) , value)
    if index is None:
        raise ValueError("value not in array")
    return index    



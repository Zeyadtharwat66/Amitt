def sum_array(arr:list):
    if arr==None:
        return None
    return sum(arr)-(max(arr)+min(arr)) if len(arr)>1 else 0
print(sum_array(None))
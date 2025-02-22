def move_zeros(lst):
    non_zero_index=0
    for i in range(len(lst)):
        if lst[i]!=0:
            lst[non_zero_index],lst[i]= lst[i], lst[non_zero_index]
            non_zero_index+=1
    return lst
print(move_zeros([1,2,0,1]))
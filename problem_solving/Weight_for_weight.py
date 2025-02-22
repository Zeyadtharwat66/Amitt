def order_weight(strng):
    arr1=strng.split()
    arr2=strng.split()
    temp=0
    for i in range(len(arr1)):
        arr1[i]=(sum(int(x) for x in arr1[i]))
    for i in range(len(arr2)):
        for j in range(len(arr2)):
            if arr1[i]<arr1[j]:
                temp=arr1[j]
                arr1[j]=arr1[i]
                arr1[i]=temp
                temp=arr2[j]
                arr2[j]=arr2[i]
                arr2[i]=temp
            elif arr1[i]==arr1[j]:
                if arr2[i]<arr2[j]:
                    temp=arr1[j]
                    arr1[j]=arr1[i]
                    arr1[i]=temp
                    temp=arr2[j]
                    arr2[j]=arr2[i]
                    arr2[i]=temp
    output=''
    for i in range(len(arr2)):
        if i!=len(arr2)-1:
            output+=arr2[i]+' '
        else:
            output+=arr2[i]
    return output
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
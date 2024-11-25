def solution(number):
    x=3
    y=5
    list3=[]
    if number <=0:
        return 0
    while number > x:
        list3.append(x)
        x+=3
    while number > y:
        list3.append(y)
        y+=5
    list3 = list(dict.fromkeys(list3))
    return sum(list3) 
print(solution(6))
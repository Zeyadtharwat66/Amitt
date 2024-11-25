def solution(s):
    l=[]
    if len(s)%2==0:
        for i in range(0,len(s),2):
            if i%2==0:
                l.append(s[i:i+2])   
    else:
        for i in range(0,len(s),2):
            if i==len(s)-1:
                l.append(s[i]+'_')
            else:
                l.append(s[i:i+2])  
    return l

print(solution("abcdefg"))  # ['ab', 'cd', 'ef', 'g']

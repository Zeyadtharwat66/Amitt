x = input().split()
x=list(map(int,x))
ans=""
for i in range(len(x)):
    x[i]=str(bin(x[i]))[2:]
for i in range(len(x[0]) if len(x[0])>len(x[1]) else len(x[1])):
    ans +=x[0][i]+x[1][i] 
print(ans)
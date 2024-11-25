def likes(names):
    s=""
    if len(names) ==0:
        return "no one likes this"
    else:
        if len(names)==1:
            return names[0]+" likes this"
        else:
            if len(names)<=3:
                s=f"{names[0]}"
                for i in range(1,len(names)-1):
                    s+=", "
                    s+=f"{names[i]}"
                s+=f" and {names[len(names)-1]} like this"
            else:
                s=f"{names[0]}, {names[1]} and {len(names)-2} others like this"
    return s
print(likes(["names","zeyad"]))
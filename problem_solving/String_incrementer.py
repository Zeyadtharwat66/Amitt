def increment_string(strng):
    i=len(strng)
    while i>0 and strng[i-1].isdigit():
        i-=1
    originalPart=strng[:i]
    numberPart=strng[i:]
    if numberPart:
        incremented_number=str(int(numberPart)+1).zfill(len(numberPart))
        return originalPart+incremented_number
    else:
        return strng+"1"


print(increment_string("foo8bar99"))
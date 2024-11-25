input = input("Enter Your mail: ")
input.lower()
count = 0
if (input.__contains__('@')):
    for x in input:
        if x == '@':
            count += 1
    if count != 1:
        print("Invalid email")
        exit()
    index = input.index('@')
    checkpoint = input[index:len(input)]
    if (not checkpoint.__contains__('.')):
        print("Invalid email")
        exit()
    username = input[0:index]
    domain = input[index+1:input.index('.')]
    domainEnding = input[len(input)-4:len(input)]
    print(username)
    print(domain)
    if (domainEnding == '.com'):
        print("Commercial Domain")
    elif (domainEnding == '.edu'):
        print("Educational Domain")
    else:
        print("Other Domain")
else:
    print("Invalid email")
    exit()

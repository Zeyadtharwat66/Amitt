def product_fib(prod):
    a,b=1,1
    while a*b<prod:
        a,b=b,a+b 
    return(a,b,a*b==prod)
print(product_fib(302))
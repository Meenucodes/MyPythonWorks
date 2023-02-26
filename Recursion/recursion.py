# calls a function repeatively
# more suitable for mathematical implementation
# can cause stack overflow

# factorial of n (n! = n(n-1)(n-2) ... 0!)
# 0! is 1

def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n-1)
    

def factorial_loop(n):
    f=1
    for i in range(1,n+1):
        f = i * f
    return f
        
    



if __name__ == '__main__':
    print("Factorial")
    print(" Factorial for {} is {} using loop".format(5, factorial_loop(5)))
    print(" Factorial for {} is {} using recursion".format(5, factorial_recur(5)))
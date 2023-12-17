# Fibonacci - 1,1,2,3,5,8,13,21,34,55 .......

## Fibonacci without memoization (Recusrion)
def fib(n):
    if n <=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
#print (fib(39)) # Starts from 1

cache = {0: 0, 1: 1}

## Fibonacci with memoization (Recusrion)
def fibonacci_of(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]

#print (fibonacci_of(40)) # Starts from 0

## Fibonacci with Iterative - Non Recusrion
def fibo(n):
    zero_value = 0
    table = [zero_value] * (n+1) # for fib(6) -> [0,1,2,3,4,5,6] starts from zero
    table[1] = 1 # Base scenarion
    for i in range(len(table)):
        #print(table[i])
        if i+1 < len(table): table[i+1] += table[i]
        if i+2 < len(table): table[i+2] += table[i]

    return table[n]

print (fibo(6))
print (fibo(7))
print (fibo(8))
print (fibo(50))
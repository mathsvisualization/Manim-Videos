from functools import lru_cache, cache

@lru_cache
def fib(n: int) -> int:
    # If the value of n is equal to or less than 1 then it will return 1
    if n<=1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
        
for i in range(0, 100):
    print(f"{i}: {fib(i)}")
    
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
    
[print(factorial(i)) for i in range(6)]

import time

def countdown(n):
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(1)
        # decrement the counter and return it as the next N val for recursive use --------
        return countdown(n-1)

# variable for the time to countdown from
x = 5
print(f"Begin countdown from {x}:")
# run the function on the var
print(countdown(x))

# Recursive factorial example ------------------
def fkt(n):
    if n == 0:
        return 1
    else:
        # ex 3 x 2 x 1 is 3!
        # same as 3 x (2 x 1) || 3 x 2!
        # n! = n * (n-1)!
        # recursively call n - 1 within the factorial function to achieve this calculation
        return n * fkt(n-1)

x = 5 # should return 120
print(f"The factorial of {x} is {fkt(x)}")

# Fibbonacci garbage yet again .....................................
#ALWAYS BEGIN WRITING WITH BASE CASES

def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

x = 11
print(f"The {x} ordinal fibbonzci number is {fib_recur(x)}")

# For any number in the fib-seq > 1, fib(n) = fib(n-1) + fib(n-2)
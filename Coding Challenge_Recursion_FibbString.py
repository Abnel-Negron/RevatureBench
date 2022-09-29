# Weekly Coding Challenge: 
# Recursion: Fibonacci String


# generate(3, ["j", "h"]) ➞ "j, h, hj"

# generate(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"

# generate(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"

# generate(1, ["f", "g"]) ➞ "invalid"
# return "invalid" if n is less than 2


def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Checks if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Checks if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
print(Fibonacci(9))
 

def factorial(n):
 # Base case: if n is 0 or 1, the factorial is 1
 if n == 0 or n == 1:
     return 1
 # Recursive case: n * factorial of (n-1)
 else:
     return n * factorial(n - 1)
# Test the function


number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")

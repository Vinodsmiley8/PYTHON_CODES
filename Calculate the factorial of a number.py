# Calculate the factorial of a number
def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

result = factorial(5)
print("Factorial:", result)
print("Help us solve the Fibonacci sequence!")
import time
# Ask the user for input
n = int(input("Please input a number:\n"))

time.sleep(2)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# Calculate the Fibonacci number and print the result
print(f"The Fibonacci number at position {n} is {fibonacci(n)}")
time.sleep(3)

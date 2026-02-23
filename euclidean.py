def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 48
num2 = 18
print(f"The GCD of {num1} and {num2} is {gcd_iterative(num1, num2)}")

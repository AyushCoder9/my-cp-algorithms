import math

def compute_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

num1 = 54
num2 = 24

lcm_result = compute_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm_result}.")

#Question
'''Checks if p is a probable prime using Fermat's Little Theorem with base 'a'.'''

def check_if_probably_prime(p, a=2):
  if p <= 1:
    return False
  return pow(a, p - 1, p) == 1

p_prime = 11
a_base = 3
print(f"{p_prime} is probably prime: {check_if_probably_prime(p_prime, a_base)}")

p_composite = 15
a_base = 3
print(f"{p_composite} is probably prime: {check_if_probably_prime(p_composite, a_base)}")


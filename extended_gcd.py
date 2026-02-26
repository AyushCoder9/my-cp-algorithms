def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def mod_inverse_manual(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"{a} has no modular inverse mod {m} (gcd is {gcd})")
    else:
        return x % m

a_val = 3
m_val = 13

try:
    inverse_manual = mod_inverse_manual(a_val, m_val)
    print(f"\nManual inverse of {a_val} mod {m_val} is: {inverse_manual}")
    print(f"Verification: ({a_val} * {inverse_manual}) % {m_val} = {(a_val * inverse_manual) % m_val}")
except ValueError as e:
    print(e)

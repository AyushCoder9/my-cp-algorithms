#Question
'''Rabin-Karp algorithm to find the pattern in the text.'''

def rabin_karp(text, pattern):

    n, m = len(text), len(pattern)
    if m == 0 or n < m:
        return []

    d = 256
    q = 101

    p_hash = 0
    t_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    results = []

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                results.append(i)

        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q

    return results


txt = "AABAACAADAABAABA"
pat = "AABA"
print(f"Pattern '{pat}' found in text at indices: {rabin_karp(txt, pat)}")

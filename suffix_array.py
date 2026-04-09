def build_suffix_array_naive(s):
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()
    return [index for suffix, index in suffixes]

text = "banana"
print(f"Suffix Array for '{text}':", build_suffix_array_naive(text))

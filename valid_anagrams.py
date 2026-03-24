'''An anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once'''
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
        
    return True

print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))

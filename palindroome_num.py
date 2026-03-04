def is_palindrome(n):
    if n < 0: return False
    
    temp = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = (reversed_num * 10) + digit
        n = n // 10
        
    return temp == reversed_num

print(is_palindrome(12321))

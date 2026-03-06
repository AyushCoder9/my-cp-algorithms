def is_balanced(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return not stack

expr1 = "{[()]}"
print(f"'{expr1}' is balanced: {is_balanced(expr1)}")

expr2 = "([)]"
print(f"'{expr2}' is balanced: {is_balanced(expr2)}")

expr3 = "{[]}"
print(f"'{expr3}' is balanced: {is_balanced(expr3)}")

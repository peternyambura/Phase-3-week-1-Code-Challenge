def is_balanced(expression):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return not stack
def is_valid_parenthesis(s):
    BRACKETS = {")": "(", "}": "{", "]": "["}

    stack = []

    for bracket in s:
        if bracket in BRACKETS:
            top_element = stack.pop() if stack else ""
            if top_element != BRACKETS[bracket]:
                return False
        else:
            stack.append(bracket)

    return True if not stack else False


print(is_valid_parenthesis("{[]}"))
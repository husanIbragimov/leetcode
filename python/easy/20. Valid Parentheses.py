def isValid(s: str) -> bool:
    stack = []
    brackets = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    for bracket in s:
        if bracket not in brackets:
            stack.append(bracket)
            continue

        if not stack:
            return False

        last_opened = stack.pop()
        if last_opened != brackets[bracket]:
            return False

    return not stack


s = "()[]{}"
print(isValid(s))

def areBracketsBalanced(str):

    openingBrackets = []
    # Keys: closing brackets (')', ']', '}')
    # Values: opening brackets ('(', '[', '{')
    bracketPairs = {')': '(', ']': '[', '}': '{'}

    if str is None:
        return True

    for i in range(len(str)):

        # It is an opening bracket, push it to the list
        if str[i] in bracketPairs.values():
            openingBrackets.append(str[i])
        # It is a closing braket, but not equal to the last opening bracket or openingBrackets is empty, returns False
        elif str[i] in bracketPairs.keys():
            if len(openingBrackets) == 0 or bracketPairs[str[i]] != openingBrackets.pop():
                return False

    # openingBrackets is not empty, return False
    if len(openingBrackets) > 0:
        return False
    else:
        return True


strs = ["([3x + 4)^2]", "[{(3x + 5) - 2}^2]/10", None, '', '[[[]]']

for i in range(len(strs)):
    print(f"{strs[i]} => {areBracketsBalanced(strs[i])}")

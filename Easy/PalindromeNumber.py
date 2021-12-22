def isPalindrome(x):
    y = str(x)
    z = len(y)
    flag = 0
    for index, char in enumerate(y):
        if char == y[z - index - 1]:
            flag += 1
        else: pass
    return flag == z

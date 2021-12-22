def sqrt(x):
    if x * x == x:
        return x
    else:
        for z in range(x+1):
            if z * z == x:
                return z
            elif z * z > x:
                return z - 1


print(sqrt(4)) #->2
print(sqrt(8)) #->2
print(sqrt(9)) #->3

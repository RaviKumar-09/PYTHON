def factorail(n):
    if n == 1:
        return True
    else:
        return n * factorail(n-1)
    
print(factorail(9))
def mystry(n):
    if n<2:
        return n
    else:
        return mystry(n-1)+mystry(n-2)
n=25
print(mystry(n))
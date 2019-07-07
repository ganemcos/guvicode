def isfloat(i):
    try:
        float(i)
        return True
    except ValueError:
        return False
print("Yes" if isfloat(input()) else "No")

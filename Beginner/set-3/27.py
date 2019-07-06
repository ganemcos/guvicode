def isfloat(i):
    try:
        float(i)
        return True
    except ValueError:
        return False
print("yes" if isfloat(input()) else "no")

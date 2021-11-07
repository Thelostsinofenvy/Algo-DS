x1 = 43
v1 = 2
x2 = 70
v2 = 2


def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return ("NO")
    if (x2-x1) == 0 or (v2-v1) == 0:
        return("NO")
    if (x1 - x2) % (v2 - v1) == 0:
        print("YES")
    else:
        print("NO")


kangaroo(x1, v1, x2, v2)

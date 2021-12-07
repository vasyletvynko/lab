import math

x1 = float(input("x1 "))
h = float(input("крок "))

eps = float(input("точність "))


def opt(w, a, b, c, h):
    print(w, a, b, c)
    if w < a:
        c = b
        while a > w:
            a -= h
    elif w > c:
        a = b
        while c < w:
            c += h
    elif w < b:
        c = b
    elif w > b:
        a = b
    else:
        w = b
    return a, w, c


def fun(a):
    return a * a + 4 * a * math.sin(a) + math.cos(a)


def find_min(h, x1):
    k = 0
    x2 = x1 + h
    f1 = fun(x1)
    f2 = fun(x2)
    if f1 > f2:
        x3 = x1 + 2 * h
        _x = x2
    else:
        x3 = x1 - h
        _x = x1
    f3 = fun(x3)

    fmin = min(f1, f2, f3)
    f_x = max(f1, f2, f3)

    x1, x2, x3 = sorted([x1, x2, x3])

    while abs((fmin - f_x) / f_x) > eps:
        x1, x2, x3 = opt(_x, x1, x2, x3, h)
        f1 = fun(x1)
        f2 = fun(x2)
        f3 = fun(x3)

        tmp = sorted([(f1, x1), (f2, x2), (f3, x3)])
        fmin, xmin = tmp[0]

        a1 = (f2 - f1) / (x2 - x1)
        a2 = (1 / (x3 - x2)) * (((f3 - f1) / (x3 - x1)) - ((f2 - f1) / (x2 - x1)))

        _x = (x2 + x1) / 2 - a1 / (2 * a2)
        f_x = fun(_x)

    return f1, f2, f3, fmin, _x


print(find_min(h, x1))
from math import sin


def f(x):
    return x**3-3*sin(x)


def dichotomy(a=0, b=1, eps=0.001):
    i = 0
    x = (a + b) / 2
    while abs(b - a) > eps:
        i += 2
        if f(x-eps) > f(x+eps):
            a = x
        else:
            b = x
        x = (a + b) / 2
    print("Метод дихотомии")
    print("Количество вычислений: " + str(i))
    print("Минимальное значение: f(" + str(x) + ")=" + str(f(x)))
    return x


def golden_section(a=0, b=1, eps=0.001):
    x1 = a + 0.382 * (b - a)
    x2 = a + 0.618 * (b - a)
    i = 2
    y1 = f(x1)
    y2 = f(x2)
    while abs(b - a) > eps:
        i += 1
        if y1 >= y2:
            a = x1
            x1 = x2
            y1 = f(x1)
            x2 = a + 0.618 * (b - a)
        else:
            b = x2
            x2 = x1
            y2 = f(x2)
            x1 = a + 0.382 * (b - a)
    x = (a + b) / 2
    print("Метод золотого сечения")
    print("Количество вычислений: " + str(i))
    print("Минимальное значение: f(" + str(x) + ")=" + str(f(x)))
    return x


dichotomy()
print("-"*20)
golden_section()

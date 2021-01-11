import matplotlib.pyplot as plt
import numpy as np


def drow_broken_line(X, f, fminus, x_rand):
    plt.title('Поиск глобального минимума методом ломаных')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(X, f(X))
    plt.plot(X, fminus(X, x_rand))
    plt.grid()
    plt.show()


def main():
    def f(x): return np.cos(x ** 2 - 3 * x) + 4
    def df(x): return -np.sin(x ** 2 - 3 * x) * (2 * x - 3)

    def fminus(x, x_rand):
        result = []
        for elem in x:
            result.append(np.max(f(x_rand) - L * np.abs(elem - x_rand)))
        return result

    eps = 0.01
    a = -1
    b = 3
    X = np.arange(a, b, eps)
    L = np.max(df(X))
    print('Константа Липшица: ' + str(round(L, 3)))

    x_rand = np.array([a, b])
    while 1:
        fstar = np.min(f(x_rand))
        P = np.array([elem for elem in X if f(elem) <= fstar])
        x_new = P[np.argmin(fminus(P, x_rand))]
        drow_broken_line(X, f, fminus, x_rand)
        if fstar - fminus(np.array([x_new]), x_rand)[0] < eps:
            print('Глобальный минимум: f(x=' + str(round(x_new, 3)) + ') = ' + str(round(f(x_new), 3)))
            break
        else:
            x_rand = np.append(x_rand, x_new)


main()

import numpy
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Для поиска следующего шага (α) будем использовать метод дихотомии на интервале (-1; 1),
# так как значения шага предполагаются маленькими.
def dichotomy(f, a, b, eps):
    x = (a + b) / 2
    while abs(b - a) > eps:
        if f(x-eps) > f(x+eps):
            a = x
        else:
            b = x
        x = (a + b) / 2
    return x


# Метод градиентного спуска рассчитывает следующую точку по формуле (x, y)_{i+1} = (x, y)_i – α * f`((x, y)_i).
# Функция возвращает список точек, полученных на каждом шаге.
# Последняя точка является найденным минимумом.
def gradient_descent(f, dfx, dfy, eps, point_0):
    def next_point(point, a): return [point[0] - a * dfx(point), point[1] - a * dfy(point)]
    points = [point_0]
    while (dfx(points[-1]) ** 2 + dfy(points[-1]) ** 2) ** 0.5 > eps:
        alpha = dichotomy(lambda a: f(next_point(points[-1], a)), -1, 1, eps)
        points.append(next_point(points[-1], alpha))
    return points


def draw_3d(points, f):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.elev, ax.azim = 30, 30
    x = []
    y = []
    z = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
        z.append(f(point))
        ax.text(x[-1]+0.01, y[-1]+0.01, z[-1]+0.01, '%s' % (str(len(x))), size=20, zorder=1, color='k')
    ax.plot(x, y, z, marker='o', color='k')
    x_srf = numpy.arange(min(x), max(x), 0.01)
    y_srf = numpy.arange(min(y), max(y), 0.01)
    xgrid, ygrid = numpy.meshgrid(x_srf, y_srf)
    zgrid = f([xgrid, ygrid])
    #ax.plot_surface(xgrid, ygrid, numpy.array(zgrid), color='w')
    plt.show()


def main():
    def f(point):
        x = point[0]
        y = point[1]
        return 6 * x**2 - 4 * x * y + 3 * y**2 + 4 * (x + 2 * y) + 22

    def dfx(point):
        x = point[0]
        y = point[1]
        return 12 * x - 4 * y + 4

    def dfy(point):
        x = point[0]
        y = point[1]
        return - 4 * x + 6 * y + 8

    eps = 0.01
    point_0 = [-2, -2]

    points = gradient_descent(f, dfx, dfy, eps, point_0)
    draw_3d(points, f)
    min_point = [round(p_i, 2) for p_i in points[-1]]
    print('f(' + str(min_point) + ') = ' + str(f(min_point)))
    print('dfx(' + str(min_point) + ') = ' + str(dfx(min_point)))
    print('dfy(' + str(min_point) + ') = ' + str(dfy(min_point)))
    print('Количество итераций: ' + str(len(points)))


main()

import numpy
import numpy as np
from cvxopt.solvers import qp
from cvxopt.base import matrix as hello
from scipy import *
from matplotlib import pyplot as pylab
import operator
from numpy import zeros, ones, identity, exp, arange
import random, math

coolalpha = []


def kernel(p1, p2):
    return sum(p * q for p, q in zip(p1, p2)) + 1


def Kernel(p1, p2):
    return sigmoidKernel(p1, p2)


def polynomialKernel(p1, p2):
    return math.pow(sum(p * q for p, q in zip(p1, p2)) + 1, 3)


def sigmoidKernel(p1, p2):
    return math.tanh(0.001 * sum(p * q for p, q in zip(p1, p2)) + 0.02)


def RBFKernel(x, y, sigma=0.1):
    sigma = 0.1
    length = np.linalg.norm(np.subtract((x[0], x[1]), (y[0], y[1])), 2)
    return math.exp(-1 * np.power(length, 2) / (2 * sigma))
    # return math.exp(-(val) / (2 * sigma * sigma))


def buildPmatrix(points):
    p = []
    for p1 in points:
        inner = []
        for p2 in points:
            inner.append(p1[2] * p2[2] * Kernel(p1, p2))
        p.append(inner)
    return p


def indicator(x):
    ind = 0
    for i, j in zip(data, alpha):

        if -1 * pow(10, -5) < j < pow(10, -5):
            coolalpha.append({'data': i, 'alpha': j})
            continue
        ind += j * i[2] * Kernel(x, i)
    return ind


def createClassA():
    return [(random.normalvariate(-1.5, 1),
             random.normalvariate(0.5, 1),
             1.0)
            for i in range(5)] + \
           [(random.normalvariate(1.5, 1),
             random.normalvariate(0.5, 1),
             1.0)
            for i in range(5)]


def createClassB():
    return [(random.normalvariate(0.5, 0.5),
             random.normalvariate(-0.5, 0.5),
             -1.0)
            for i in range(10)]


classA = createClassA()
classB = createClassB()

data = classA + classB
random.shuffle(data)

P = buildPmatrix(data)
q = ones(len(data)) * -1
G = identity(len(data)) * -1
h = zeros(len(data))

# solve the linear equation
r = qp(hello(P), hello(q), hello(G), hello(h))

# pick out the alphas
alpha = list(r['x'])

xrange = numpy.arange(-4, 4, 0.05)
yrange = numpy.arange(-4, 4, 0.05)

grid = matrix([[indicator((x, y))
                for y in yrange]
               for x in xrange])

pylab.hold(True)
pylab.plot([p[0] for p in classA],
           [p[1] for p in classA],
           'bo')

pylab.plot([p[0] for p in classB],
           [p[1] for p in classB],
           'ro')

# pylab.plot([hej['data'][0] for hej in coolalpha],
#            [hej['data'][1] for hej in coolalpha],
#            'ko')

pylab.contour(xrange, yrange, grid,
              (-1.0, 0.0, 1.0),
              colors=('red', 'black', 'blue'),
              linewidths=(1, 3, 1))

pylab.show()

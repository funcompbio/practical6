import numpy as np

def f(X, c) :
    dX = c*X
    return(dX)

def euler(X0, c, t) :
    X = np.zeros(len(t))
    X[0] = X0
    h = t[1] - t[0]
    i = 0
    while (i < (len(t)-1)) :
        X[i+1] = X[i] + h * f(X[i], c)
        i = i + 1

    return(X)

## set time points between 0 and 2 in steps (h) of 0.1
t = np.arange(0, 2, 0.1)

## initial value
X0 = 1

## constant for dX = c X
c = 2

## integrate dX = c X with Euler's method
X = euler(X0, c, t)

## print resulting values for each time point
print("t,dX")
i = 0
while (i < len(X)) :
    print("%.2f,%.2f" %(t[i], X[i]))
    i = i + 1

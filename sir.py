import numpy as np

def f(I, rho, alpha) :
    dI = rho * I * (1-I) - alpha * I
    return(dI)

def euler(I0, rho, alpha, t) :
    I = np.zeros(len(t))
    I[0] = I0
    h = t[1] - t[0]
    i = 0
    while (i < (len(t)-1)) :
        I[i+1] = I[i] + h * f(I[i], rho, alpha)
        i = i + 1

    return(I)

def main(rho, alpha) :
  ## set time points between 0 and 50 in steps (h) of 1
  t = np.arange(0, 30, 1)

  ## initial value
  I0 = 0.001

  ## integrate dI = rho * I * (1 - I) - alpha * I with Euler's method
  I = euler(I0, rho, alpha, t)

  ## print resulting values for each time point
  print("t,dI")
  i = 0
  while (i < len(I)) :
      print("%.3f,%.3f" %(t[i], I[i]))
      i = i + 1

if __name__ == "__main__" :
    import sys

    if (len(sys.argv) != 3) :
        print("error: sir.py <rho> <alpha>")
    else :
        main(float(sys.argv[1]), float(sys.argv[2]))




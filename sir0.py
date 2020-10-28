def main(rho, alpha) :
    I = 0.1
    dI = rho * I * (1-I) - alpha * I
    return(dI)

if __name__ == "__main__" :
    import sys

    if (len(sys.argv) != 3) :
        print("error: sir.py <rho> <alpha>")
    else :
        print(main(float(sys.argv[1]), float(sys.argv[2])))




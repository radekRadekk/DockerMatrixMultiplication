import sys
from datetime import datetime


def mnoz(dane):
    A = dane[0]
    X = dane[1]

    nrows = len(A)
    ncols = len(A[0])
    y = []
    for i in range(nrows):
        s = 0
        for c in range(0, ncols):
            s += A[i][c] * X[c][0]

        # sleep(0.01)
        y.append(s)

    return y


def read(fname):
    f = open(fname, "r")
    nr = int(f.readline())
    nc = int(f.readline())

    A = [[0] * nc for x in range(nr)]
    r = 0
    c = 0
    for i in range(0, nr * nc):
        A[r][c] = float(f.readline())
        c += 1
        if c == nc:
            c = 0
            r += 1

    return A


start = datetime.now()

ncpus = int(sys.argv[1]) if len(sys.argv) > 1 else 2
fnameA = sys.argv[2] if len(sys.argv) > 2 else "../Data/bigA.dat"
fnameX = sys.argv[3] if len(sys.argv) > 3 else "../Data/bigX.dat"

A = read(fnameA)
X = read(fnameX)

original_stdout = sys.stdout

with open('out.txt', 'w') as f:
    sys.stdout = f  # Change the standard output to the file we created.
    print(f'Wynik y={mnoz([A, X])}')
    sys.stdout = original_stdout  # Reset the standard output to its original value

end = datetime.now()
delta = end - start
print(f"Execution time in seconds: {delta.total_seconds()}")

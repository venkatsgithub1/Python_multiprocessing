from multiprocessing import Pool
import time


def f(n):
    sum_var = 0
    for x in range(1000):
        sum_var += x**2
    return n**2


if __name__ == "__main__":
    t1 = time.time()

    # Pool takes argument process=number (number of processes).
    p = Pool()

    result = p.map(f, range(10000))

    p.close()
    p.join()

    print(time.time() - t1)

    t1 = time.time()
    res = []
    for x in range(10000):
        res.append(f(x))

    print(time.time() - t1)

import time


def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n**2)


def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n**3)


arr = [2, 3, 8, 9]

t = time.time()
calc_square(arr)
calc_cube(arr)

print('time taken', time.time() - t)

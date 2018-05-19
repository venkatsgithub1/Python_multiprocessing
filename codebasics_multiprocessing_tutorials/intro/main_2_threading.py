import time
# importing threading module
import threading


def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n**2)


def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n**3)


arr = [2, 3, 8, 9]

t = time.time()

t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print('time taken', time.time() - t)

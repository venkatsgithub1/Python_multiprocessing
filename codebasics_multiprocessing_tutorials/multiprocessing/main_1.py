import time
import multiprocessing

square_res = []


def calc_square(numbers):
    global square_res
    print("calculate square of numbers")
    for n in numbers:
        # time.sleep(5)
        print('square:', n**2)
        square_res.append(n**2)
    print('res inside method:', square_res)


# def calc_cube(numbers):
#     print("calculate cube of numbers")
#     for n in numbers:
#         time.sleep(5)
#         print('cube:', n**3)


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    t = time.time()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    # p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()

    print('time taken:', time.time() - t)

    print('res:', square_res)
    print("Done!")

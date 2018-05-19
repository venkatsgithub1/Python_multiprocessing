import multiprocessing


def calc_square(numbers, result, v):
    v.value = 5.67
    print("calculate square of numbers")
    for idx, n in enumerate(numbers):
        result[idx]=n**2
    print('res inside process:', result[:])


if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array('i', len(numbers))
    v=multiprocessing.Value('d',0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()

    print('outside process:', result[:], v.value)

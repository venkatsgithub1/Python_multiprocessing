import multiprocessing

def calc_square(numbers, q):
    print("calculate square of numbers")
    for n in numbers:
        q.put(n**2)
    print('res inside process:', q)


if __name__ == "__main__":
    numbers = [2, 3, 5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while not q.empty():
        print(q.get())

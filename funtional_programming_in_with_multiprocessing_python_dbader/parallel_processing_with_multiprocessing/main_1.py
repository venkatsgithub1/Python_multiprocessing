import collections

scientist = collections.namedtuple('scientist', [
    'name', 'field', 'born', 'nobel'
])

scientists = (
    scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

import time

import os


def transform(x):
    print("processing", x.name, "process:", os.getpid())
    time.sleep(1)
    result = {'name': x.name, 'age': 2018 - x.born}
    print("processing complete for", x.name, "process:", os.getpid())
    return result


import multiprocessing

start = time.time()

# sequential
# result = tuple(map(
#     transform,
#     scientists
# ))

# pool = multiprocessing.Pool()
pool = multiprocessing.Pool(processes=len(scientists))
result = pool.map(transform, scientists)


print("time taken:", (time.time() - start))

print(result)

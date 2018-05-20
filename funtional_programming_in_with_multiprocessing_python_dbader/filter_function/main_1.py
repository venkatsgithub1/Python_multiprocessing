import collections

scientist = collections.namedtuple('Scientist', [
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

print(tuple(filter(lambda x: x.nobel, scientists)))
print(tuple(filter(lambda x: x.field == 'physics' and x.nobel, scientists)))
print(tuple(filter(lambda x: x.field == 'math', scientists)))

print([x for x in scientists if x.nobel])

# improvement
print(tuple(x for x in scientists if x.nobel))

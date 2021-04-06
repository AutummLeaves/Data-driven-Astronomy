import timeit

x = lambda a : a + 10


print(timeit.timeit(lambda :x(5)))


def test(x):
	a = x + 10
	return a

print(timeit.timeit(lambda :test(5)))


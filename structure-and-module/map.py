def cube(x): return x*x*x


print(list(map(cube, range(1, 11))))

seq = range(8)
def square(x): return x*x


print(list(zip(seq, map(square, seq))))

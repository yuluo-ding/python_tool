# /user/bin/python
# -*- coding: utf-8 -*-

g = (x * x for x in range(10))
for n in g:
    # print n
    pass

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b , a+b
        n = n+ 1

for n in fib(6):
    print n


def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

list(r)

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print str2int('13579')

def ad(x, y):
    return x * y

def prod(L):
    return reduce(ad, L)

L = [1, 3, 5]
print prod(L)

# print reduce(lambda x, y: x*y , [1, 3, 5])

# def str2float(s):
#     def f(x, y):
#         return x * 10 + y
#     m = s.find('.')
#     L1 = s[:m]
#     L2 = s[m+1:len(s)]
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#     return reduce(f, map(char2num, L1)) + reduce(lambda x, y : x * 0.1 + y, map(char2num, L2)) * 0.1**len(len(s)-m-1)
#
# print  str2float('123.456')

def odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def not_divisible(n):
    return lambda x: x%n > 0

def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible, n)

for n in primes():
    if n < 1000:
        print n
    else:
        break
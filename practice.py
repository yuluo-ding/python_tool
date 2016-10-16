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

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]

for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
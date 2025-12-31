import math
a, b = map(int, input().split())
A, B = a, b

while b:
    a,b = b, a % b

print(a)

print(A // a * B)

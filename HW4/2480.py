a, b, c = input().split()
first = int(a)
second = int(b)
third = int(c)
if (first == second == third):
    print(10000 + (first * 1000))
elif (first == second):
    print(1000 + (first * 100))
elif (second == third):
    print(1000 + (second * 100))
elif (first == third):
    print(1000 + (first * 100))
else:
    print(max(first, second, third) * 100)

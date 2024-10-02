a=int(input())
b=int(input())
friends=[]
count=0
for i in range(b):
    first, second = input().split()
    num_first = int(first)
    num_second = int(second)
    if (num_first == 1):
        friends.append(num_second)
    if (num_second == num_first):
            friends.append(num_second)

print(c)

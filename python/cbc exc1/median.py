list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1 += list2

print(list1)

length = len(list1)
d2 = int(length/2)
if length % 2: #odd
    print(list1[d2])
else:
    print((list1[d2] + list1[d2-1])/2)
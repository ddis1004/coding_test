N = int(input())

num_list = list(map(int, input().split()))

#XOR == 다르면 1
for idx, i in enumerate(num_list):
    num_list[idx] = bin(i)



print(num_list)




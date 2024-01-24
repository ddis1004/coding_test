list = list(map(int, input().split()))

total_amount = sum(list)
if total_amount % len(list) > 0:
    print(-1)
else:
    amount_each = int(sum(list)/len(list))
    max_now
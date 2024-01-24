n = int(input())
a = []
m = [[0, 0, 0] for i in range(n)]
#print(m)
for i in range(n):
    a.append(int(input()))

m[0][0] = 0
m[0][1] = a[0]
m[0][2] = 0

def drink_through(i):
    #print(f'stage: {i+1}')
    #print(f'{m[i]}')
    m[i+1][0] = max(m[i][0], m[i][1], m[i][2])
    m[i+1][1] = m[i][0] + a[i+1]
    m[i+1][2] = m[i][1] + a[i+1]
    #print(f'{m[i+1]}')

for i in range(n-1):
    drink_through(i)

print(max(m[n-1]))
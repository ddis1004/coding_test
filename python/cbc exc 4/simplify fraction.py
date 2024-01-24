ja, mo = map(int, input().split())

def todecimal(ja, mo):
    a = '9'
    two_count = 0
    five_count = 0
    while mo % 2 == 0:
        mo = int(mo/2)
        two_count += 1
    while mo % 5 == 0:
        mo = int(mo/ 5)
        five_count += 1


    while not int(a) % mo == 0:
        a += '9'

    to_multiply = int(int(a)/mo)
    mo = int(a)

    ja *= to_multiply

    final_modifier = max(five_count, two_count)

    if two_count > five_count:
        ja *= 5 ** abs(five_count - two_count)
    if two_count < five_count:
        ja *= 2 ** abs(two_count - five_count)

    print(f'[{ja} / {mo}] * 10^(-{max(two_count,five_count)})')

    if ja > mo:
        ja

print(todecimal(ja, mo))
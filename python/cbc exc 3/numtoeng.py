N = int(input())

def convertEng(N):
    string = ""

    divider = 1000
    three_digit_cut = []

    while N > 0:
        three_digit_cut.append(N % divider)
        N = int(N/divider)

    print(three_digit_cut)

    def three_digit_Eng(M):
        if M == 0:
            return 'zero'

        def teen(M):
            if M == 11:
                return 'eleven'
            elif M == 12:
                return 'twelve'
            elif M == 13:
                return 'thirteen'
            elif M == 14:
                return 'fourteen'
            elif M == 15:
                return 'fifteen'
            elif M == 16:
                return 'sixteen'
            elif M == 17:
                return 'seventeen'
            elif M == 18:
                return 'eighteen'
            elif M == 19:
                return 'nineteen'
            elif M == 10:
                return 'ten'

        def one_digit_Eng(M):
            if M == 1:
                return 'one'
            elif M == 2:
                return 'two'
            elif M == 3:
                return 'three'
            elif M == 4:
                return 'four'
            elif M == 5:
                return 'five'
            elif M == 6:
                return 'six'
            elif M == 7:
                return 'seven'
            elif M == 8:
                return 'eight'
            elif M == 9:
                return 'nine'

        def second_digit_Eng(M):
            if M == 1:
                return None
            elif M == 2:
                return 'twenty'
            elif M == 3:
                return 'thirty'
            elif M == 4:
                return 'fourty'
            elif M == 5:
                return 'fifty'
            elif M == 6:
                return 'sixty'
            elif M == 7:
                return 'seventy'
            elif M == 8:
                return 'eighty'
            elif M == 9:
                return 'ninety'
        third = int(M/100)
        M %= 100
        second = int(M / 10)
        M %= 10
        first = M

        answer = ""
        if not third == 0:
            answer += one_digit_Eng(third) + ' hundred'
        if second == 1:
            if not third == 0:
                answer += " "
            answer += (teen(second * 10 + first))
        else:
            if not second == 0:
                answer += " " + second_digit_Eng(second)
            if not first == 0:
                answer += " " + one_digit_Eng(first)
        return answer

    answer = ""
    len3 = len(three_digit_cut)

    if len3 > 3: #billion
        answer += three_digit_Eng(three_digit_cut[3]) + ' billion'
    if len3 > 2: #million
        if three_digit_cut[2] > 0:
            answer += three_digit_Eng(three_digit_cut[2]) + ' million'
    if len3 > 1: #thousand
        if three_digit_cut[1] > 0:
            answer += three_digit_Eng(three_digit_cut[1]) + ' thousand'
    if len3 > 0: #one
        if three_digit_cut[0] > 0:
            answer += three_digit_Eng(three_digit_cut[0])

    return answer

print(convertEng(N))
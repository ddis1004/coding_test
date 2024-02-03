#수열이 주어질 때 i번째 elemnt 제외한 element를 곱한 값을 return하는 함수를 구현하라
#제한사항 O(n)

array = [1, 2, 3, 4]

def noMeMultiply(S: list):
    from_left_multiply = 1
    from_right_multiply = 1

    left_array = []
    right_array = []

    for i in range(len(S)):
        from_left_multiply *= S[i]
        from_right_multiply *= S[len(S) - i - 1]
        left_array.append(from_left_multiply)
        right_array.append(from_right_multiply)

    answ = []

    for i in range(len(S)):
        answ.append(left_array[i] * right_array[len(S) - i - 1])

    return answ


print(noMeMultiply(array))
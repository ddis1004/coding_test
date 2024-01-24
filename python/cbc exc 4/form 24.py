from itertools import permutations

numbers = list(map(int, input().split()))

possible_order = permutations([0,1, 2, 3])


def possible_numbers(start, end, number_list):
    answer = []
    if start == end:
        return [number_list[start]]
    elif end - start == 1:
        a = number_list[start]
        b = number_list[end]
        if a + b not in answer:
            answer.append(a + b)
        if a - b not in answer:
            answer.append(a - b)
        if a * b not in answer:
            answer.append(a * b)
        return answer
    elif end - start == 2: # three number between them
        left2 = possible_numbers(start, start + 1, number_list)
        for i in left2:
            if i + number_list[end] not in answer:
                answer.append(i + number_list[end])
            if i - number_list[end] not in answer:
                answer.append(i - number_list[end])
            if i * number_list[end] not in answer:
                answer.append(i * number_list[end])
        right2 = possible_numbers(start + 1, start + 2, number_list)
        for i in right2:
            if i + number_list[start] not in answer:
                answer.append(i + number_list[start])
            if i - number_list[start] not in answer:
                answer.append(i - number_list[start])
            if i * number_list[start] not in answer:
                answer.append(i * number_list[start])
        return answer
    elif end - start == 3:
        left3 = possible_numbers(0, 2, number_list)
        #print(left3)
        for i in left3:
            if i + number_list[3] == 24:
                return True
            if i - number_list[3] == 24:
                return True
            if i * number_list[3] == 24:
                return True
        right3 = possible_numbers(1, 3, number_list)
        #print(right3)
        for i in right3:
            if i + number_list[0] == 24:
                return True
            if i - number_list[0] == 24:
                return True
            if i * number_list[0] == 24:
                return True
        left2 = possible_numbers(0, 1, number_list)
        right2 = possible_numbers(2, 3, number_list)
        #print(left2, right2)
        for i in left2:
            for j in right2:
                if i + j == 24:
                    return True
                if i - j == 24:
                    return True
                if i * j == 24:
                    return True
        return False

def wrapper():
    for order in possible_order:
        number_list = []
        for o in order:
            number_list.append(numbers[o])
        if possible_numbers(0, 3, number_list):
            print(True)
            return
    print(False)
    return
wrapper()
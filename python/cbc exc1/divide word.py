str = input()
word_list = list(input().split())


def find_word(str):
    word_checklist = [1 for i in range(len(word_list))]

    def check_word(i, c):
        count = 0
        for idx, check in enumerate(word_checklist):
            if check == 1:
                if not word_list[idx][i] == c:
                    #print(f'i : {i}, c: {c}, idx: {idx}')
                    word_checklist[idx] = 0
                else:
                    count += 1
        return count

    def reset_checklist():
        for i in range(len(word_checklist)):
            word_checklist[i] = 1

    def print_word():
        for idx, check in enumerate(word_checklist):
            if check == 1:
                print(word_list[idx])
                return idx

    cursor = 0
    start = 0
    while cursor < len(str):
        if check_word(cursor - start, str[cursor]) == 1:
            word_num = print_word()
            #print(f'before /// start: {start}, cursor : {cursor}')
            start += len(word_list[word_num]) - (cursor - start) #line that moves cursor to start of next word
            cursor = start
            #print(f'after /// start: {start}, cursor : {cursor}')
            reset_checklist()
        else:
            cursor += 1



find_word(str)

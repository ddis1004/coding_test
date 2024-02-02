from itertools import combinations

N, K = map(int, input().split())

words = []
total_chars = []

#remove common char
for i in range(N):
    word = input()
    chars = []
    for c in word:
        if c not in ['a', 'n', 't', 'i', 'c']:
            if c not in chars:
                chars.append(c);
            if c not in total_chars:
                total_chars.append(c);

    words.append(chars)

def count_words(chars, words):
    count = 0
    for w in words:
        c_count = 0
        for c in w:
            if c not in chars:
                break
            else:
                c_count += 1
        if c_count == len(w):
            count+= 1
    return count

def learn_maximum_word(K, total_chars):
    if K < 5:
        return 0
    answ = 0
    K -= 5
    combination = list(combinations(total_chars, min(K, len(total_chars))))
    for com in combination:
        answ = max(count_words(com, words), answ)
    return answ

print(learn_maximum_word(K, total_chars))

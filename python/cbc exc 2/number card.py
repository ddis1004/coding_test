N = int(input())
HAND = list(map(int, input().split()))
M = int(input())
SEARCH_TARGET = list(map(int, input().split()))

HAND = sorted(HAND)
SEARCH_TARGET = sorted(SEARCH_TARGET)

def find_cards(hand, search_target):
    
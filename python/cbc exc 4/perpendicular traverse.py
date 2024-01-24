import math

tree1 = [3, 9, 20, None, None, 15, 7]
tree2 = [1, 2, 3, 4, 5, 6, 7]

def vertical_traverse(tree):
    stack = []
    tree_of_vertical = [0 for i in range(len(tree))]

    stack.append((0, int(math.log2(len(tree))))) #(index, vertical)
    tree_of_vertical[0] = int(math.log2(len(tree)))
    while stack:
        i = stack.pop()
        if i[0] * 2 + 1 < len(tree) and not tree[i[0]* 2 + 1] == None:
            stack.append((i[0] * 2 + 1, i[1] - 1))
            tree_of_vertical[i[0] * 2 + 1] = i[1] - 1
        if i[0] * 2 + 2 < len(tree) and not tree[i[0] * 2 + 2] == None:
            stack.append((i[0] * 2 + 2, i[1] + 1))
            tree_of_vertical[i[0] * 2 + 2] = i[1] + 1

    print(tree_of_vertical)
    answer = []
    for i in range(0, max(tree_of_vertical) + 1, 1):
        temp = []
        for idx, j in enumerate(tree):
            if tree_of_vertical[idx] == i and not j == None:
                temp.append(j)
        temp = sorted(temp)
        answer.append(temp)
    print(answer)


vertical_traverse(tree2)
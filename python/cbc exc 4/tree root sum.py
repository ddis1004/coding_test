tree1 = [1,2,3]
tree2 = [-10, 9, 20, None, None, 15, 7]

def sum_of_subtree(idx, tree):
    #get left, right value
    if idx > len(tree) - 1 or tree[idx] is None:
        return {'route_max': 0, 'max': 0}
    left_return = sum_of_subtree(idx * 2 + 1, tree)
    left = left_return['route_max']
    right_return = sum_of_subtree(idx * 2 + 2, tree)
    right = right_return['route_max']

    # return largest between myself, left + myself, right + myself, left + myself + right
    #print(f'left: {left} , right : {right}, this : {tree[idx]}')

    return {'route_max': max(left + tree[idx], right + tree[idx], tree[idx]),
                         'max': max(left, right, tree[idx], left + tree[idx], right + tree[idx], left + right + tree[idx], left_return['max'], right_return['max'])}


shit = sum_of_subtree(0, tree2)
print(shit['max'])

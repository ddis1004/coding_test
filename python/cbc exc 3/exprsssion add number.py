digits = int(input())
target = int(input())

list_digits = list(map(int, list(str(digits))))

operators = ['+', '-', '*', '']
def possible_expression(list_digits, target):
    #+, - , * possible
    answer = []

    def create_expression(prev, idx):

        if idx == len(list_digits) - 1:
            # evaluate the expression
            expression = ''
            for idx, op in enumerate(prev):
                expression += str(list_digits[idx])
                expression += op
            expression += str(list_digits[-1])
            #print(expression, '=', eval(expression))
            if eval(expression) == target:
                answer.append(expression)
            return
        else:
            for op in operators:
                if list_digits[idx] == 0 and op == '':
                    continue
                prev.append(op)
                create_expression(prev, idx + 1)
                prev.pop()

    create_expression([], 0)
    return answer

print(possible_expression(list_digits, target))

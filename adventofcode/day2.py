def get_input():
    inputs = []
    print('enter the input')
    while True:
        value = input()
        if value != 'end':
            inputs.append(value)
        else:
            return inputs
            break


def stone_paper_scissor_one(inputs):
    new_list = [list(x) for x in inputs]
    count = 0
    for i in new_list:
        if i[0] == 'A' and i[2] == 'X':
            count += 4  # rock and rock -> draw (3+1)
        elif i[0] == 'A' and i[2] == 'Y':
            count += 8  # rock and paper -> win (6+2)
        elif i[0] == 'A' and i[2] == 'Z':
            count += 3  # rock and scissor -> lose (0+3)
        elif i[0] == 'B' and i[2] == 'X':
            count += 1  # paper and rock -> lose (0+1)
        elif i[0] == 'B' and i[2] == 'Y':
            count += 5  # paper and paper -> draw (3+2)
        elif i[0] == 'B' and i[2] == 'Z':
            count += 9  # paper and scissor -> win (6+3)
        elif i[0] == 'C' and i[2] == 'X':
            count += 7  # scissor and rock -> win(6+1)
        elif i[0] == 'C' and i[2] == 'Y':
            count += 2  # scissor and paper -> lose(0+2)
        elif i[0] == 'C' and i[2] == 'Z':
            count += 6  # scissor and scissor -> draw(3+3)
    return print(f'result: {count}')


stone_paper_scissor_one(get_input())


def stone_paper_scissor_two(inputs):
    new_list = [list(x) for x in inputs]
    count = 0
    for i in new_list:
        if i[0] == 'A' and i[2] == 'X':
            count += 3  # rock and scissor -> lose (0+3)
        elif i[0] == 'A' and i[2] == 'Y':
            count += 4  # rock and rock -> draw (3+1)
        elif i[0] == 'A' and i[2] == 'Z':
            count += 8  # rock and paper -> win (6+2)
        elif i[0] == 'B' and i[2] == 'X':
            count += 1  # paper and rock -> lose (0+1)
        elif i[0] == 'B' and i[2] == 'Y':
            count += 5  # paper and paper -> draw (3+2)
        elif i[0] == 'B' and i[2] == 'Z':
            count += 9  # paper and scissor -> win (6+3)
        elif i[0] == 'C' and i[2] == 'X':
            count += 2  # scissor and paper -> lose (0+2)
        elif i[0] == 'C' and i[2] == 'Y':
            count += 6  # scissor and scissor -> draw (3+3)
        elif i[0] == 'C' and i[2] == 'Z':
            count += 7  # scissor and rock -> win (6+1)
    return print(f'result: {count}')


stone_paper_scissor_two(get_input())

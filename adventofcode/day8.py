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


def find_visible_trees(inputs):
    for i in inputs:
        for j in i:
            print(j)

    # print(inputs)



find_visible_trees(get_input())

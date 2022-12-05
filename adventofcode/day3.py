def advent_function():
    count = 0
    is_continue = True
    while is_continue:
        value = input()
        if value != 'end':
            total_length = int(len(value) / 2)
            first_string, second_string = value[:total_length], value[total_length:]
            for i in first_string:
                for j in second_string:
                    if i == j:
                        first_string.replace(i, "", total_length)
                        second_string.replace(j, "", total_length)
                        if i.islower():
                            count += ord(i) - 96
                            break
                        elif i.isupper():
                            count += ord(i) - 38
                            break

        else:
            is_continue = False
    return count


print(advent_function())


def _advent_function():
    count = 0
    first_list = []
    is_continue = True
    while is_continue:
        value = input()
        first_list.append(value)
        if value != 'end':
            if len(first_list) == 3:
                second_list = list(set(first_list[0]) & set(first_list[1]) & set(first_list[2]))
                first_list.clear()
                if second_list[0].islower():
                    count += ord(second_list[0]) - 96
                elif second_list[0].isupper():
                    count += ord(second_list[0]) - 38

        else:
            is_continue = False
    return count


print(_advent_function())

# x = 0
# y = 4
# z = set()
# value = input()
# for i in value:
#     for i in value[x:y]:
#         z.add(i)
#     print('1: ', z)
#     if len(z) == 4:
#         print(y-1)
#         break
#     else:
#         x += 1
#         y += 1

# is_continue = True
# while is_continue:
#     value = input()
#     print('1', value)
#     input_list = list(value)
#     if value != 'end':
#         if
#     else:
#         is_continue = False

value = input()
input_list = list(value)
count = 0
for i in value:
    new_set = set(input_list[input_list.index(i): input_list.index(i)+4])
    count += 1
    if len(new_set) == 4:
        print(count+3)
        break
    new_set.clear()
    input_list.remove(i)


value = input()
input_list = list(value)
count = 0
for i in value:
    new_set = set(input_list[input_list.index(i): input_list.index(i)+14])
    count += 1
    if len(new_set) == 14:
        print(count+13)
        break
    new_set.clear()
    input_list.remove(i)


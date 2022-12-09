import re
from collections import defaultdict

# with open('input.txt') as file:
#     for line in file:
#         print(line.rstrip())

# with open('input.txt') as file:
#     lines = [line.rstrip() for line in file]
#     print(lines)

# with open('input.txt', 'r') as i:
#     output = list(map(lambda l: l.replace("\n", ""), i.readlines()))
#     print(output)


def get_sizes():
    sizes = defaultdict(int)
    # print('sizes: ', sizes)
    sizes["/root"] = 0
    with open('input.txt', 'r') as i:
        # print('initial output: ', i)
        output = list(map(lambda l: l.replace("\n", ""), i.readlines()))
        # print('final output: ', output)
    curr_folder = "/root"
    for line in output:
        # print('line: ', line)
        cmd = re.search(r'\$ (cd|ls) (.+)', line)

        # print('cmd: ', type(cmd))
        if cmd:
            # print('cmd group: ', cmd.groups())
            op, folder = cmd.groups()
            # print('op: ', op)
            # print('folder: ', folder)
            if op in ["dir", "ls"]: continue
            if op == "cd":
                if folder == "/":
                    curr_folder = "/root"
                elif folder == "..":
                    curr_folder = curr_folder[0:curr_folder.rfind("/")]
                else:
                    curr_folder += f'/{folder}'
        file_size = re.search(r'(\d+) (.+)', line)
        # print('file_size: ', file_size)
        if file_size:
            size, file = file_size.groups()
            folder = curr_folder
            for _ in range(curr_folder.count("/")):
                sizes[folder] += int(size)
                folder = folder[:folder.rfind("/")]
    #     print('repeat the cycle')
    # print('sizes: ', sizes)
    return sizes


def part_01():
    sizes = get_sizes()
    total = 0
    for size in sizes.values():
        if size <= 100000:
            total += size
    print(f"Part 1: {total}")


def part_02():
    sizes = get_sizes()
    target = sizes["/root"] - 39999999
    folders = []
    for size in sizes.values():
        if target <= size:
            folders.append(size)
    print(f"Part 2: {min(folders)}")


part_01()
part_02()





#
# def get_sizes():
#     sizes = defaultdict(int)
#     print('sizes: ', sizes)
#     sizes["/root"] = 0
#     with open('input.txt', 'r') as i:
#         print('initial output: ', i)
#         output = list(map(lambda l: l.replace("\n", ""), i.readlines()))
#         print('final output: ', output)
#     curr_folder = "/root"
#     for line in output:
#         print('line: ', line)
#         cmd = re.search(r'\$ (cd|ls) (.+)', line)
#         # print('cmd: ', type(cmd))
#         if cmd:
#             op, folder = cmd.groups()
#             print('op: ', op)
#             print('folder: ', folder)
#             if op in ["dir", "ls"]: continue
#             if op == "cd":
#                 if folder == "/":
#                     curr_folder = "/root"
#                 elif folder == "..":
#                     curr_folder = curr_folder[0:curr_folder.rfind("/")]
#                 else:
#                     curr_folder += f'/{folder}'
#         file_size = re.search(r'(\d+) (.+)', line)
#         print('file_size: ', file_size)
#         if file_size:
#             size, file = file_size.groups()
#             folder = curr_folder
#             for _ in range(curr_folder.count("/")):
#                 sizes[folder] += int(size)
#                 folder = folder[:folder.rfind("/")]
#         print('repeat the cycle')
#     print('sizes: ', sizes)
#     return sizes

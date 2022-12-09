from typing import Dict
import re

ContactDict = Dict[str, str]


def check_if_valid(contacts: ContactDict) -> bool:
    for name, email in contacts.items():

        if (not isinstance(name, str)) or (not isinstance(email, str)):
            return False

        if not re.match(r"[a-zA-Z0-9\._\+-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$", email):
            return False
    return True


print(check_if_valid({'Dhanesh': 'dk@gmail.com'}))
print(check_if_valid({'Deepak': 'deep@i2i.com', 123: 'wrg@name.com'}))

from typing import NewType

StudentID = NewType('StudentID', int)


def get_student_name(stud_id: StudentID) -> str:
    return str(input(f'Enter username for ID #{stud_id}:\n'))


stud_a = get_student_name(StudentID(100))
print(stud_a)

# This is incorrect!!
stud_b = get_student_name(-1)
print(stud_b)


# def display_list(a: list) -> float:
#     print(a)
#
#
# display_list([1, 2, 3, ])
#
#
# def display_list(a: list) -> None:
#     print(a)


# display_list([1, 2, 3, ])

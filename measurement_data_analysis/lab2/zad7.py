in_dict = {'a': 5, 'b': 7, 'c': 4}
in_l1 = ['a', 'b', 'c']
in_l2 = ['a', 'b', 'd']


def try_except_ex(d, l):
    for key in l:
        if key not in d:
            raise ValueError


try:
    try_except_ex(in_dict, in_l1)
    print("Ok")
except ValueError:
    print("Value_Error")

try:
    try_except_ex(in_dict, in_l2)
    print("Ok")
except ValueError:
    print("Value_Error")

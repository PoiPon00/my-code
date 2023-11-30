

def zad_7_func(tup):
    el1 = [tup[i] for i in range(len(tup))]
    dic = { el1[i]: tuple([k+1 for k in range(len(tup)) if k+1 != el1[i] ]) for i in range(len(tup)) }
    return dic
input_tuple = (1, 2, 3, 4, 5)
print(zad_7_func(input_tuple))
list_1 =[1,2,3,4,15]
list_2 =[3,4,5,6]
list_3 =[6,7,8]
list_4 =[8,9,10]
def extend_list(*args):
 exli = []
 for arg in args:
    for item in arg:
        if item not in exli:
            exli.append(item)
 return sorted(exli)
print(extend_list(list_1,list_2,list_3))
print(extend_list(list_1,list_2,list_3,list_4))
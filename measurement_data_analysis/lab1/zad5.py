def extend_lists(*arg):
 exli=[]
 for i in range(len(arg)):
        exli.extend(arg[i])
 exli=sorted(exli)
 p=0
 while p<(len(exli)-1):
         if (exli[p]==exli[p+1]):
            exli.remove(exli[p])
         p=p+1
 return sorted(exli)

list_1=[1, 2, 3, 4, 15]
list_2=[3, 4, 5, 6]
list_3=[6, 7, 8]
list_4=[8, 9 ,10]
print(extend_lists(list_1, list_2, list_3))
print(extend_lists(list_1, list_2, list_3, list_4))
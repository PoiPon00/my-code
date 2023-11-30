list = [1, 5, 8]
list.append(17)
print(list)
li = [i*5 for i in list]
print(li)
li.remove(min(li))
print(li)



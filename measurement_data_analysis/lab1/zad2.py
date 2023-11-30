def multiply_lists(x,y):
 li3=[]
 for i in range(len(x)):
   li3.append(x[i]*y[i])
 return li3
list_1=[i for i in range(0,10,2)]
list_2=[i for i in range(1,11,2)]
list_3=multiply_lists(list_1, list_2)
print(list_1)
print(list_2)
print(list_3)


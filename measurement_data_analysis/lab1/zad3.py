list_1 = [i for i in range(0,10,2)]
list_2 = [i for i in range(1,11,2)]
multiply_lists = lambda li1,li2: [li1[i]*li2[i] for i in range(len(li1))]
list_3 = multiply_lists(list_1,list_2)
print(list_1)
print(list_2)
print(list_3)

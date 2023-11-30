def my_multiply(l):
    def in_func(number):
        for i in range(len(l)):
            l[i]=l[i]*number
        return l
    return in_func


example_list = [1,2,3,4,5]
in_func = my_multiply(example_list)
print(example_list)
in_func(5.5)
print(example_list





example_list = [1,2,3,4]
example_func = my_multiply(example_list)
print(example_list)
print(example_func(5.5))


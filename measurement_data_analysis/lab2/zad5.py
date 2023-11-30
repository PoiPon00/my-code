def my_multiply(number):
    def in_func(l):
        for i in range(len(l)):
            l[i]=l[i]*number
        return l
    return in_func

in_func = my_multiply(5.5)
example_list = [1,2,3,4,5]
print(example_list)
in_func(example_list)
print(example_list)

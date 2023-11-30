def zad_6_func(*arg):
    count = 0
    dic = {}
    prime = 0
    for i in arg:
        count = count + 1
    if (count % 2 == 0) or (count == 1):
        l = [i for i in arg]
        dic = {(i, l[i]) for i in range(len(l))}
        print(dic)
    else:
        if (count < 2):
            x = "False"
        for j in range(2, count):
            if(count % j == 0):
                x = "False"
        else:
            x = "True"
        print(x)
zad_6_func(5, 7, 4, "Temperatura", 5, "Natezenie")
zad_6_func(2, 3, 5)
zad_6_func(2, 9, 11, 5, 7, 2, 1, 4, 6)





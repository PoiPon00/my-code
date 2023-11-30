def add_dictionaries(x,y):
  d3={}
  for key in x:
         if (key in x)==(key in d3):
           d3[key]+=x[key]
         else:
           d3[key]=x[key]
  for key in y:
         if (key in y)==(key in d3):
          d3[key]+=y[key]
         else:
          d3[key]=y[key]
  return d3
dict_1={'a':5, 'b':7, 'c':13}
dict_2={'c':15, 'd':3, 'e':-5}
dict_3=add_dictionaries(dict_1, dict_2)
print(dict_1)
print(dict_2)
print(dict_3)
my_dict = {'Dima' : 1988, 'Marina' : 1986, 'Lesha' : 1983, 'luba' : 1980, 'Sasha' : 1977}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Denis'))
my_dict.update({'Anton': 1970, 'Max': 1975})
a = my_dict.pop('Marina')
print(a)
print(my_dict)

my_set = {1, 2, 3, 1, 3, 'aplle', 'aplle', 'cheery'}
print(my_set)
my_set.update({5, 'orange', (1,3,5)})
my_set.discard(1)
print(my_set)
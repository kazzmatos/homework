my_dict={'Maria':1929, 'Boris':1955, 'Alya':1963, 'Mark':1926}
print('Dict:',my_dict)
print('Existing value:',(my_dict['Maria']))
print('Not existing value:',my_dict.get('Valera'))
my_dict.update({'Valera':1949, 'Lyubov':1947})
print('Deleted value:',my_dict.pop('Valera'))
print('Modified dictionary:',my_dict)
my_set={1,2,1,2,3,False,2.5,2.5,'string','string'}
print('Set:',set(my_set))
my_set.update((10000,'none'))
my_set.discard('none')
print('Modified set:',my_set)
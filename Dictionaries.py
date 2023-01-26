# Словари хранят значение (ключ-значение) Синтаксис: {'key1': "value1", 'key2': "value2"}
my_dictionary = {'apples': "red", 'melon': "yellow"}
print(my_dictionary ['melon'])

# В качестве значения можно указать список и словарь в словаре
a = {"dict1": 164, "dict2": [7,8,4], "dict3": {'apples': 50}}
print(a["dict1"])
print(a["dict2"])
print(a["dict3"]['apples'])
print(a["dict2"][1])

b_dict = {'lst': ['a','b','c','d']}
print(b_dict['lst'][2].upper())

#Добавление в словарь:
d = {'num':10, 'num1': 20}
d['num2'] = 300
print(d)
d['num2'] = 500
print(d)
print(d.keys())

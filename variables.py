# модуль 1 - описание объекта и проверка типов данных

# str
name_object = 'банан'
print('наименование объекта : ', name_object, ', тип переменной : ', type(name_object))

# int
count_object = 7
print('кол-во объектов ', name_object, ', тип переменной : ', type(count_object))

# float
t_object = 12.5
print('температура хранения объекта ', name_object, ', тип переменной : ', type(t_object))

# bool
sale_1 = 3
sale_2 = 4
print('продано кол-во объектов : ', sale_1, ', значит все объекты проданы ?', sale_1 == count_object,
      ', тип переменной : ', type(sale_1 == count_object))
print('продано кол-во объектов : ', sale_1 + sale_2, ', значит все объекты проданы ?',
      (sale_1 + sale_2) == count_object, ', тип переменной : ', type((sale_1 + sale_2) == count_object))

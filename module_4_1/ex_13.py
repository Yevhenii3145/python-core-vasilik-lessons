# обьединение множеств
numbers = {1, 2, 3, 4, 5}
test = {4, 5, 6, 7, 8}
a = numbers | test  # обьединим 2 сета убирая дубликаты
print(a)

b = numbers & test  # пересечение 2 сетов {4, 5}
print(b)


# удаляем из 1 сета все элементы которые есть во 2 сете
c = numbers - test
print(c)
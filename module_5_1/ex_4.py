"""
Метод: isdigit
----
1.Найти количество цифр в строке
2.Найти количество чисел в строке
"""
string = "Нильс Бор родился в семье профессора физиологии Копенгагенского университета Христиана Бора (1858-1911) и Эллен Адлер (1860-1930). Родители Бора поженились в 1881 году.Отца Нильса Бора дважды выдвигали кандидатом на Нобелевскую премию по физиологии или медицине [11] . Мать была дочерью влиятельного и весьма состоятельного еврейского банкира и парламентария-либерала Давида Баруха Адлера [ da] (1826-1878) и Дженни Рафаэл (1830-1902) из ​​британской еврейской банкирской династии Raphael Raphael & sons .1 августа 1912 года [13] в Копенгагене Нильс Бор женился на Маргарет Норлунд, сестре близкого друга его брата Гаральда — Нильса Эрика Норлунда, с которой Нильс Бор познакомился в 1909 году [14] .Всего у Нильса и Маргарет было шесть детей (один сын, Христиан, погиб в юном возрасте). Один из них, Оге Бор , также стал выдающимся физиком, лауреатом Нобелевской премии ( 1975 ).Брат Нильса Бора Гаральд был известным математиком ."


def count_digits(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count


print(count_digits(string))


def count_numbers(string):
    count = 0
    pos = 0
    nums = []
    while pos < len(string):
        if string[pos].isdigit():  # проверяем являетя ли строка чилом
            num = ""
            # ищем окончание числа
            while pos < len(string) and string[pos].isdigit():
                num += string[pos]  # записываем число
                pos += 1  # увеличиваем индекс на единицу
            nums.append(num)
            count += 1  # увеличиваем счетчик на единицу
        else:
            pos += 1
    return (count, nums)


print(count_numbers(string))

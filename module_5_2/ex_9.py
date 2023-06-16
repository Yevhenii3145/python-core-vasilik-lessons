'''
Завдання: Пошук email
- алфавіт, який використовується для назви email, - англійська
- префікс (все, що знаходиться до символу @) починається з латинської літери і може містити будь-яке число або літеру,
включаючи нижнє підкреслення та символ крапки, складається щонайменше з двох символів
- суфікс (все, що знаходиться після символу @) складається тільки з букв англійського алфавіту, складається
з двох частин, розділених точкою, і доменне ім'я верхнього рівня не може бути менше двох символів (все, що після крапки)
'''

import re
text = "Ima_Fool@YTna.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.ua 12Fool1@iana.org"

result = re.findall(r"\b[a-zA-Z][\w_.]+@[a-zA-Z]+\.?[a-zA-Z]{0,2}[.]?", text)
print(result)

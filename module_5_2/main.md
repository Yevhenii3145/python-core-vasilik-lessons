.    один любой символ, кроме строки \n
?    0 или 1 вхождение шаблона слева, тоесть он вставится после чего-то (после выражения)
+    1 и больше вхождений шаблона слева, он также ставится после выражения
*    0 и больше вхождений шаблона слева
\w   любая цифра или буква [a-zA-Z0-9_] (\W -все, кроме буквы или цифры [^a-zA-Z0-9_]) \ - это экранированный символ
\d   любая цифра [0-9 (\D - всё, кроме цифры [^0-9])]
\s   любой символ пробела [\t\n\r\f\v] (\S - всё, кроме не пробельного символа [\t\n\r\f\v]])
\b   граница слова
[..]  один из символов в скрбках ([^..]) - любой символ, кроме тех, которые в скобках)
\    экранирование спец.символов (пример: \. - означает точку или \+ - знак "плюс"),
тоесть используется для поиска символов которые уже заняты
^ и $  начало и конец строки соответственно (^ это не тоже самое что и [^])
{n,m}  от n до m вхождений (пример: {,m} - от нуля до m), пример {\d,3} - будет искать 3 цифры
a|b    соответствует a или b
()    групирует выражение и возвращает найденный текст, используются для поиска ссылок,email.С ними всё сложно
\t,\n,\r  символ табуляции, новой строки и возврат коретки.

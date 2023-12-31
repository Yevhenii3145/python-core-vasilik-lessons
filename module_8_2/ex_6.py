"""
Генрация автомобильного номера.Две литеры, четыре цифры,две литеры.
Для Киевской области код AI
Последние две литеры из списка: A, B, C, E, H, I, K, M, O, P, T, X
(используются украинские литеры, которые имеют графические соответствия в латыни)
"""

import random

start = "AI"
set_of_letters = ["A", "B", "C", "E", "H", "I", "K", "M", "O", "P", "T", "X"]
set_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

numbers = "".join(random.choices(set_of_numbers, k=4))
last_l = "".join(random.choices(set_of_letters, k=2))

print(f"{start} {numbers} {last_l}")  # AI 3679 KM

print(f"{''.join(random.choices(set_of_letters, k=2))} "
      f"{''.join(random.choices(set_of_numbers, k=4))} "
      f"{''.join(random.choices(set_of_letters, k=2))}")  # PE 5720 KB

# List: Например, для температур нужно учесть ошибку и повысить каждую температуру на 0.5 градуса.

temps = [0.5, 0.0, -3.5, 0.0, 2.0, 3.5, 0.5, -
         4.0, -3.5, -0.5, -3.5, -10.5, -14.0, -1.0, -1.0]

fix_t = [t + 0.5 for t in temps]
# [1.0, 0.5, -3.0, 0.5, 2.5, 4.0, 1.0, -3.5, -3.0, 0.0, -3.0, -10.0, -13.5, -0.5, -0.5]
print(fix_t)

unique_t = {t + 0.5 for t in temps}
print(unique_t)  # {0.5, 1.0, 2.5, 0.0, 4.0, -0.5, -3.5, -13.5, -10.0, -3.0}

dict_t = {t: t + 0.5 for t in temps}
# {0.5: 1.0, 0.0: 0.5, -3.5: -3.0, 2.0: 2.5, 3.5: 4.0, -4.0: -3.5, -0.5: 0.0, -10.5: -10.0, -14.0: -13.5, -1.0: -0.5}
print(dict_t)
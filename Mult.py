# Таблица умножения.

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{j} * {i} = {i * j:1} \t', end='')
    print('')
else:
    print("Готово")

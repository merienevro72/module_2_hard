x = int(input ('введите число от 3 до 20: '))
result = []
for n in range (1,20):
    for m in range (n+1,20):
        if x % (n+m) == 0:
            result.append(n)
            result.append(m)
print (f'пароль для {x}: {''.join(map(str, result))}')




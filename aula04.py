a = int(input('Entre com o número: '))

div = 0
for x in range(1, a + 1):
    resto = a % x
    print(a, resto)
    if resto == 0:
        div = div + 1

if div == 2:
    print('número {} e primo'.format(a))
else:
    print('número {} não e primo'.format(a))

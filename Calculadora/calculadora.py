##Calculadora em Python
##Cabeçalho Calculadora

print('Calculadora em Python')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
##input da opção desejada

op = input("escolha uma opção:")
op = int(op)
print(op)

if (op == 1):
    num1 = int(input('Escolha um valor:'))
    num2 = int(input('Escolha um segundo valor'))
    soma = (num1 + num2)
    print(soma)

elif op == 2:
    num1 = int(input('Escolha um valor:'))
    num2 = int(input('Escolha um segundo valor'))
    sub = num1 - num2
    print(sub)

elif op == 3:
    num1 = int(input('Escolha um valor:'))
    num2 = int(input('Escolha um segundo valor'))
    mult = num1 * num2
    print(mult)

elif op == 4:
    num1 = int(input('Escolha um valor:'))
    num2 = int(input('Escolha um segundo valor'))
    divs = num1 + num2
    print(divs)

else:
    op = input("escolha uma opção válida:")
    print(op)
    
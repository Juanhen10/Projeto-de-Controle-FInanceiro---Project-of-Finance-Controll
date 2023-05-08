from os import system

# 022170 - senha

system('cls')
# basicamente será um controle financeiro, onde vocÇe vai colocar os seus gastos no mês.
# seja comida, lazer, etc.

# por exemplo esse mês já gastei:
# em essencial: 291,31
# em lazer: 303,46

# observações. gastei mais em lazer do que ensencial, isso não pode ocorrer!!!


def linha(text='', s='*'):
    if len(text):
        a = len(text) * s
        print(a)
        print(text)
        print(a)


def painel(mes='', essencial=0, lazer=0, total=0, total_pago=0, previsto=0.0):
    linha(mes)
    print(f'O seu essencial no mês: R${essencial:.2f}')
    print(f'seus lazer foi: R${lazer}')
    print(f'total no mês: R${total:.2f}')
    print(f'seus total pago: R${total_pago}')
    resta = total - total_pago
    print(f'Ainda falta a pagar: R${resta:.2f}')
    print(f'valor previsto: R${previsto}')
    print('-'*20)
    s = previsto - resta
    if s > 0:
        print(f'Você lucrou: R${s:.2f}')
    else:
        print(f'você negativou: R${s:.2f}')


def soma(*args):
    t = sum(args)
    return (t)


# essencial = soma(36.97, 17.09, 15, 22.90, 58.83, 21.25,
#                  20, 15, 142.48, 20, 15, 20, 15, 192.65, 40.5)
# lazer = soma(55, 122.50, 8.50, 73.71, 2)
# total = essencial + lazer
# total_pago = soma(50, 4.90, 150, 200, 37, 20)
# resta_pagar = total - total_pago
# valor_previsto = 372
salario = 372 + 432.45
linha(f'Salario: R${salario:.2f} ')

# painel('Abril', essencial, lazer, total, total_pago,
#        resta_pagar, valor_previsto)
essencial = soma(15, 20, 14.90, 20, 56.04, 124.90, 15, 20, 50, 23)
lazer = soma(20, 122.49, 73.70, 22.30, 20.50, 39, 60, 72, 10, 77.95, 32)
total = essencial + lazer
pagos = soma(10)
a = total - pagos
painel('Maio', essencial, lazer, total, pagos, salario)

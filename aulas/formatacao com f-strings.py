# s == string
# d == int
# f == float
# .<numero de difityos>f
# x or X == hexadecimal
# (Caractere)(><^)(quantidade)
# > == esquerda
# < == direita
# ^ == centro
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Convertion flags == !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.489816516544:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')

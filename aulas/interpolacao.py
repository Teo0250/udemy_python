# """ 
# Interpolação básica de strings
# s == string
# d and i == int
# f == float
# x and X == hexadecimal (ABCDEF0123456789)
# """

nome = 'Teo'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500))
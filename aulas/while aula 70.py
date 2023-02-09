frase = 'Ta maluco cara que sono é esse que eu estou sentido!'

i = 0
qtd_show = 0
l_ma = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_show_atual = frase.count(letra_atual)

    if qtd_show < qtd_show_atual:
        qtd_show = qtd_show_atual
        l_ma = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi ' f'"{l_ma}" que apareceu ' f'{qtd_show}x')

  
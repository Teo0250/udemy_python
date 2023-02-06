numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)

    if numero_int % 2 == 0:
        print('O número é par')
    elif numero % 2 != 0:
        print('O número é ímpar')

else:
    print('Não é um número inteiro')


#########################################################################################

hora = input('Digite o um horário: ')

hora_int = int(hora)

try:
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite!')
    else:
        print('Não é um horário válido!')

except:
    print('Digite um número inteiro!')

# ###########################################################################################

primeiro_nome = input('Digite o seu primeiro nome: ')

tam_nome = len(primeiro_nome)

if primeiro_nome == '':
    print('Você não informou seu nome!')
elif tam_nome <= 4:
    print('Seu nome é muito curto')
elif tam_nome > 4 and tam_nome <= 6:
    print('Seu nome é normal')
elif tam_nome > 6:
    print('Seu nome é muito grande')
    

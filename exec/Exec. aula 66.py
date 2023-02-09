while True:
    n1 = input('Digite um número: ')
    op = input('Escolha um operador (+-/*): ')
    n2 = input('Digite outro número: ')

    n_validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        n_validos = True
    except:
        n_validos = None

    if n_validos is None:
        print('Um ou mais números digitados são inválidos!')
        continue
    
    op_permitidos = '+-/*'

    if op not in op_permitidos:
        print('Operador não permitido!')
        continue
    
    if len(op) > 1:
        print('Digite somente um operador.')
        continue
    
    print('Realizando a sua conta!')
     
    if op == '+':
        print(f'{n1_float} + {n2_float} = ', n1_float + n2_float)
    elif op == '-':
        print(f'{n1_float} - {n2_float} = ', n1_float - n2_float)
    elif op == '/':
        print(f'{n1_float} / {n2_float} = ', n1_float / n2_float)
    elif op == '*':
        print(f'{n1_float} * {n2_float} = ', n1_float * n2_float)

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
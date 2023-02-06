"""
CONSTANTE = 'Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
    \ - barra invertida pode quebrar linhas no meio do codigo EX:
    if local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        local_carro >= (LOCAL_1 - RADAR_RANGE):
"""
## TUDO MINÚSCULO É ENTENDIVEL COMO VARIAVEL
velocidade = 61 #velocidade atual do carro
local_carro = 102 #local em que o carro está na estrada

## TUDO EM MAIÚSCULO É ENTENDIVEL COMO CONSTANTE
RADAR_1 = 60 #Velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #a distáncia onde o radar pega

if velocidade > RADAR_1:
    if local_carro <= (LOCAL_1 + RADAR_RANGE) or local_carro >= (LOCAL_1 - RADAR_RANGE):
        print('multado')
    else:
        print('Não multado')
else:
    print('Passou abaixo da velocidade limite! NÃO MULTADO')

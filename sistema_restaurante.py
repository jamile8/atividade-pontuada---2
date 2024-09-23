"""
Informe o número da turma: 
Turma - G93313

Nome completo dos componentes.
1 - Jamile Souza Reis
2 - Luana dos Santos Conceição
"""


import os

# Limpa o terminal.
os.system("cls || clear") 

print("\n======= Cardápio =======")

codigo_salvo = int(input("""
código = 109 - Picanha
código =  208 - Lasanha
código = 307 - Strogonoff
código = 406 - Bife Acebolado
código = 506 - Macarrão feito ao vapor
código = 605 - Parmegiana
código = 704 - Feijão Preto
                         """))

while True:
    codigo = int(input("Digite o código do seu prato: "))
    if codigo - codigo_salvo:
        print("Código inválido, Digite o código novamente: ")
    else:
        print("Deseja fazer outro pedido? ")

"""
Informe o número da turma: 
Turma - G93313

Nome completo dos componentes.
1 - Jamile Souza Reis
2 - Luana dos Santos Conceição
"""

import os
os.system("cls || clear") 

print("\n======= Cardápio =======")

print("""
código = 109 - Picanha - R$ 82.59
código =  208 - Lasanha - R$ 29.99
código = 307 - Strogonoff - R$ 34.50
código = 406 - Bife Acebolado - R$ 50.00
código = 506 - Macarrão feito ao vapor - R$ 22.00
código = 605 - Parmegiana - R$ 25.70
código = 704 - Feijão Preto - R$ 18.99""")

valor = []
pratos = []
pagamento = []
desconto = 0
total = 0




while True:
    codigo = int(input("\nDigite o código do seu prato (ou 0 para finalizar): "))
    if codigo == 0:
        break
    else:
        match codigo:
            case 109:
                    valor.append(82.59)
                    pratos.append("109 - Picanha")
            case 208:
                valor.append(29.99)
                pratos.append("208 - Lasanha")
            case 307:
                valor.append(34.50)
                pratos.append("307 - Strogonoff")
            case 406:
                valor.append(50.00)
                pratos.append("406 - Bife acebolado")
            case 506:
                valor.append(22.00)
                pratos.append("506 - Marracarrão")
            case 605:
                valor.append(25.70)
                pratos.append("605 - Parmegiana")
            case 704:
                valor.append(18.99)
                pratos.append("704 - Feijão preto")
            case _:
                print("Código inválido. Tente novamente.")

    print("Prato adicionado. Deseja fazer mais algum pedido?")

valor_total = sum(valor)

while True:
    forma_pagamento = input("Escolha a forma de pagamento ( V - á Vista, C Cartão de crédito): ")
    if forma_pagamento in ("V" , "v"):
        desconto = valor_total * 0.10
        total = valor_total - desconto
        pagamento = " Á Vista"
        break
    elif forma_pagamento in ( "C" , "c"):
        valor_total * 0.10
        total = valor_total + desconto
        pagamento = "Cartão de crédito"
        break
    else:
        print("Forma de pagamento inválida. Tente novamente")


print(f"\nTotal: R$ {valor_total: .2f}")
print(f"Pratos escolhidos: {pratos}")
print(f"Forma de pagamento: {pagamento}")
print(f"Valor do desconto ou acréscimo aplicado: R$ {desconto: .2f}")
print(f"Valor total a ser pago: R$ {total: .2f}")
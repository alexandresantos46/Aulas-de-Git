print ("Área de Pagamento")
 
# O cliente irá inserir o valor da sua compra
valor_venda = float(input("Digite o valor da compra: "))

# Tipos de pagamento
pagamento = ("0 - Pix",
             "1 - Boleto",
             "2 - Crédito a Vista",
             "3 - Crétido Parcelado")

# Aparecerá na tela os metodos de pagamento disponíveis
print ("Os metodos de pagamento são: ")
print (pagamento)

""" O cliente vai escolher o metodo de pagamento,
o numero a esquerda corresponte o metodo de pagamento,
exemplo:
0 para Pix"""

forma_pagamento = int(input("Escolha o metodo de pagamento: "))

# Aparecerá na tela o metodo de pagamento escolhido
print ("A forma de pagamento escolhida é: ")
print (pagamento[forma_pagamento])

# Para pix o cliente ganhará 15% de desconto
if forma_pagamento == 0:
  print ("Você ganhou 15% de desconto, o valor final da compra é: ",valor_venda - valor_venda * 0.15)

# Para boleto o cliente ganhará 5% de desconto
elif forma_pagamento == 1:
  print ("Você ganhou 5% de desconto, o valor final da compra é: ",valor_venda - valor_venda * 0.05)

# Para credito a vista o cliente não ganhará desconto
elif forma_pagamento == 2:
  print ("O valor final da compra é: ",valor_venda)

# Para credito parcelado o cliente não ganhará desconto e deverá escolher a quantidade de parcelas
else:
  quantidade_parcelas = int(input("Escolha a quantidade de parcelas: "))
  print ("O valor final da compra é ",valor_venda,
         "parcelado em ",quantidade_parcelas,
         "vezes, o valor de cada parcela é de: ",valor_venda / quantidade_parcelas)

print ("Resumo da Compra")

print ("O valor da compra é: ",valor_venda)
print ("A forma de pagamento é: ")
print (pagamento[forma_pagamento])
if forma_pagamento == 0:
  print ("O valor final da compra é: ",valor_venda - valor_venda * 0.15)
elif forma_pagamento == 1:
  print ("O valor final da compra é: ",valor_venda - valor_venda * 0.05)
elif forma_pagamento == 2:
  print ("O valor final da compra é: ",valor_venda)
else:
  print ("O valor final da compra é: ",valor_venda,"parcelado em: ",quantidade_parcelas,"vezes")

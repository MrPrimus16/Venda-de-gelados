#Apresentação do programa de venda de cupuaçu e açaí
print("Olá, bem vindo a loja de gelados paraenses do Julianno Arthur!!!")

#Aprsentação do cardápio de gelados:
print("                      Cardápio:")
print("--- | Tamanho | ---  | Cupuaçu(CP) | --- |  Açaí(AC) |")
print("--- |    P    | ---  |  R$ 9.00    | --- | R$ 11.00  |")
print("--- |    M    | ---  |  R$ 14.00   | --- | R$ 16.00  |")
print("--- |    G    | ---  |  R$ 19.00   | --- | R$ 21.00  |")

#Tamanho do Cupuaçu(CP):
PCP = 9.00
MCP = 14.00
GCP = 19.00
#Tamanho do Açaí(AC):
PAC = 11.00
MAC = 16.00
GAC = 21.00

#Variável para acumular o valor total da compra:
acumulador = 0.00

#dados para coletar da compra do  cliente:
while True:
  Tamanho = input("Digite o tamanho do gelado (P/M/G): ").upper()
  Sabor = input("Digite o sabor do gelado (CP/AC): ").upper()

  #Condicionais para tamanho e sabor do gelado:
  if Tamanho == "P" and Sabor == "CP":
    acumulador += PCP
    print(f"Você pediu sabor cupuaçu do tamanho P: R${PCP:.2f}")
  elif Tamanho == "P" and Sabor == "AC":
    print(f"Você pediu sabor açaí do tamanho P: R${PAC:.2f}")
  elif Tamanho == "M" and Sabor == "CP":
    acumulador += MCP
    print(f"Você pediu sabor cupuaçu do tamanho M: R${MCP:.2f}")
  elif Tamanho == "M" and Sabor == "AC":
    acumulador += MAC
    print(f"Você pediu sabor açaí do tamanho M: R${MAC:.2f}")
  elif Tamanho == "G" and Sabor == "CP":
    acumulador += GCP
    print(f"Você pediu sabor cupuaçu do tamanho G: R${GCP:.2f}")
  elif Tamanho == "G" and Sabor == "AC":
    acumulador += GAC
    print(f"Você pediu sabor açaí do tamanho G:R${GAC:.2f}")
  elif Sabor not in ["CP", "AC"]:
    print("Ops! Sabor inválido, tente novamente.")
  elif Tamanho not in ["P", "M", "G"]:
    print("Ops! tamanho inválido, tente novamente.")

  algo = input("Gostaria de mais algo? (S/N) ")
  if algo.upper() == "S":
    continue
  elif algo.upper() == "N":
    print(f"O valor da compra será de R${acumulador:.2f}")
    print("Obrigado por comprar na loja do Julianno!!!")
    break
  else:
    print("Opção inválida, tente novamente")
    print(f"O valor a ser pago: R${acumulador:.2f}")
    continue
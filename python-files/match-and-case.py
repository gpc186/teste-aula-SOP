print("Selecione uma das opções:\n")
print("1 - Uma coisa")
print("2 - Outra coisa")
print("3 - NDA")
opcao = int(input())

match opcao:
  case 1:
    print("Você escolheu uma coisa")
  case 2:
    print("Você escolheu outra coisa")
  case 3:
    print("Você escolheu nenhuma")
  case _:
    print("Opção inválida")
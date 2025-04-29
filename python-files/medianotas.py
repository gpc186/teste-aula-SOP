
qtdnotas = float(input("Quantas notas serão inseridas: "))

if qtdnotas != int(qtdnotas):
  print("Insira uma quantidade valida")

soma = 0

contador = 0

while contador < qtdnotas:

  contador += 1
  notaidv = float(input(f"informe a nota {contador}: "))
  if 0 <= notaidv > 10:
    print("Nota invalida, por favor insira outra nota")
    break
  soma += notaidv

media = soma / qtdnotas
print(f"A média é {media}")

if(media >= 7):
    print("Você passou")
else:
    print("Você não passou")


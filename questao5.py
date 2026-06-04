#Receber as notas em float
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

#Calcular a média
media = (nota1 + nota2 + nota3) / 3

#Exibir a média e Aprovação/Reprovação
print("A média das notas é:", f"{media:.2f}")
if media >= 7:
    print("APROVADO")
else:
    print("REPROVADO")

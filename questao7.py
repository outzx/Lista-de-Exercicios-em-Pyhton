#receber a palavra
palavra = input("Digite uma palavra: ")

#criar variável para as vogais
vogais = "aeiouAEIOUáéíóúÁÉÍÓÚ"

#Conta as vogais
total = sum(1 for letra in palavra if letra in vogais)

#Mostra o resultado
print(f"A palavra '{palavra}' tem {total} vogais.")

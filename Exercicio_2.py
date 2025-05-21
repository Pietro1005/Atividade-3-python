palavra = input("Digite uma palavra: ")


vogais = 'aeiouAEIOU'

contador_vogais = 0

for letra in palavra:
    if letra in vogais:
        contador_vogais += 1  

print(f"Total de vogais: {contador_vogais}")

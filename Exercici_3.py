numeros = []

for i in range(3):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

numeros_multiplicados = [num * 2 for num in numeros]

print(f"Lista original: {numeros}")
print(f"Lista com os números multiplicados por 2: {numeros_multiplicados}")

soma_original = sum(numeros)
soma_multiplicados = sum(numeros_multiplicados)

print(f"Soma dos números originais: {soma_original}")
print(f"Soma dos números multiplicados por 2: {soma_multiplicados}")

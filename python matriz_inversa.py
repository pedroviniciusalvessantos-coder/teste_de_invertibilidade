import numpy as np

print("=== TESTE DE INVERTIBILIDADE ===")

# Escolher tamanho da matriz
n = int(input("Digite o tamanho da matriz (2 ou 3): "))

if n not in [2, 3]:
    print("Tamanho inválido!")
    exit()

matriz = []

print("\nDigite os valores da matriz:")

for i in range(n):
    linha = []
    for j in range(n):
        valor = float(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

matriz = np.array(matriz)

print("\nMatriz digitada:")
print(matriz)

# Determinante
det = np.linalg.det(matriz)
print(f"\nDeterminante: {det:.2f}")

# Teste de invertibilidade
if det != 0:
    print("A matriz é invertível.")

    inversa = np.linalg.inv(matriz)

    print("\nMatriz inversa:")
    print(inversa)

else:
    print("A matriz NÃO é invertível (determinante = 0).")
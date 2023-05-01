vet = [0] * 10
for i in range(10):
    vet[i] = int(input("Digite um número: "))
repetidos = []
for i in range(10):
    for j in range(i+1, 10):
        if vet[i] == vet[j] and vet[i] not in repetidos:
            repetidos.append(vet[i])
            print(f"O número {vet[i]} se repete nas posições {i+1} e {j+1}.")
if len(repetidos) == 0:
    print("Não há números repetidos no vetor.")

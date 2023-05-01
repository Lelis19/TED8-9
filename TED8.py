numero = [0] * 20
for i in range(20):
    numero[i] = int(input("Digite um número: "))
print("Os números lidos, na ordem inversa, são: ")
for i in range(19, -1, -1):
    print(numero[i])
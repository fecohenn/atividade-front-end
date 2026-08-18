altura = float(input("Digite sua altura: "))
genero = int(input("Digite seu gênero (1 para masculino, 2 para feminino): "))
altura = [altura]
genero = [genero]
masculino = []
feminino = []
pessoas_femininos = 0
media_masculino = 0
media = 0
maior = 0
menor = 0
for i in range(15):
    altura.append(float(input("Digite sua altura: ")))
    genero.append(int(input("Digite seu gênero (1 para masculino, 2 para feminino): ")))
    if genero[i] == 2:
        pessoas_femininos += 1
    if genero[i] == 1:
        masculino.append(altura[i])
media = sum(altura) / len(altura)
maior = max(altura)
menor = min(altura)
media_masculino = sum(masculino) / len(masculino)
print ("A media masculina é: ", media_masculino)
print("A quantidade de pessoas do gênero feminino é: ", pessoas_femininos)
print("A maior altura é: ", maior)
print("A menor altura é: ", menor)

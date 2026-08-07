from random import randint

chave = randint(0, 100)
tentativas = 0


print("descubra o valor da chave !")
print("ela está entre 0 e 100")

while True:
    valor = int(input("valor: "))

    if chave > valor:
        print("chave eh maior que o valor\n")
        tentativas += 1

    elif chave < valor:
        print("chave eh menor que o valor\n")
        tentativas += 1

    else:
        print("valor e chave iguais !\b")
        break

print(f"tentativas ao todo = {tentativas}")
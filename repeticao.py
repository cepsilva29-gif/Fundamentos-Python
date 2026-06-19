#Repetição com uso do FOR


#grito = "Gol!"

#for letra in grito:
    #print(letra)

#print("A torcida terminou de gritar!!")

#for cobranca in range(1, 6):
    #print(f"Cobrança {cobranca} : o jogador ajeita a bola...")

#for rodada in range (1, 6):
    #print(f"Rodada {rodada} da copa do mundo")

    #if rodada == 3:
        #print("Ultima rodada! Jogo decisivo!!!")

gols_brasil = 0

for lance in range (1, 4):
    print(f"lance perigoso, numero {lance}")

    resultado = input("Foi gol do Brasil? Digite sim ou não: ")

    if resultado == "sim":
        gols_brasil += 1
        print("Gooooooooooooooooool do Brasil")
    else:
        print("Não foi gol...")

print("Fim do jogo!")
print(f"Total de gols do Brasil:{gols_brasil}")
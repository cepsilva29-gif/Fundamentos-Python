#distancia_do_gol = 20

#if distancia_do_gol < 18 :
    #print("Entrou na area.  Perigo de gol!")


#exercicio 2: If e Else

#forca_do_chute = 87
#reflexo_goleiro = 60

#if forca_do_chute > reflexo_goleiro:
    #print("Gol")
#else:
    #print("Goleiro defendeu!")


#exercicio 3: If,Elif, Else:

#gravidade_da_falta ="grave" #leve, moderada, e grave

#if gravidade_da_falta =="leve":
    #print("So advertencia!")

#elif gravidade_da_falta == "moderada":
    #print("Cartao amarelo!")

#else:           
    #print("Cartao vermelho!")   

#exercicio 4 e 5: Multiplos elif

#saldo = 1 #diferença de gols(negativo = perdendo)

# pyrefly: ignore [missing-import]
#from Trilha-Python-2026.01 - Fundamentos da Linguagem.decisao1 import saldo
    #if saldo >= 3:
#    print("Vitoria Tranquila")
#elif saldo == 2:
#    print("Jogo Controlado")
#elif saldo == 1:
#    print("Vitoria Apertada")
#elif saldo == 0:
#    print("Jogo foi empatado")
#elif saldo == -1:
#    print("Time esta perdendo")
#else:
    #print("Time esta horrivel")
    
#exercicio 5: If alinhado -> operadores logicos (AND, OR e NOT)

#teve_gol =True  
#revisao_do_var ="legal" # legal, impedido, mao, falta

#if  teve_gol:
    #print("Gol marcado.!")

    #if revisao_do_var =="legal":
        #print("Gol confirmado.!")

    #else:
        #print("Gol anulado.")
    
#else:
    #print("Não teve gol.")

#if teve_gol and revisao_do_var =="legal":# com o and se as duas condições forem verdadeiras, o código será executado.
    #print("Gol marcado!")
#else:
    #print("Gol anulado")

#pontos = 6
#saldo_gols = 3
#jogo_direto_contra_lider = Fals
#gols_marcados = 7

#if pontos >= 7 and saldo_gols > 3:
    #print("Ja esta na liderança!") 

#elif pontos == 6 and jogo_direto_contra_lider and saldo_gols >= 3:
    #print("Depende só da vitoria")   

#elif pontos == 6 and (saldo_gols < 3 or gols_marcados < 5):
    #print("Precisa ganhar e tocer")

#elif pontos < 4 or saldo_gols < -2:
    #print("Risco de eliminação!")

#else:
    #print("Classificação indefinida!")


#match case usado para verificar condições de uma variável.

revisao_do_var = "impedimento"  #legal, impedimento, mao, falta

match revisao_do_var:
    case "legal":
        print("Gol confirmado!")
    case "impedimento":
        print("Gol anulado por impedimento!")
    case "mao":
        print("Gol anulado por toque de mão!")
    case "falta":
        print("Gol anulado por falta!")
    case _:
        print("Revisão indefinida!")

        
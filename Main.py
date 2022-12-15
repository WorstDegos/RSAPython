from GeradorPrimo import GeradorNumeroPrimo
from GeradorChaves import Chaves
from cripto import Criptografia


opcao = 0

while opcao != 3:

    print("Deseja selecionar os números primos ou gerar primos aleatórios?\n[1] - Primos Aleatórios;\n[2] - Selecionar Primos;\n[3] - Sair do codificador\n\n")
    opcao = int(input("Opção selecionada:  "))
    
    if (opcao == 1 and opcao != 3):

        p = GeradorNumeroPrimo()
        numero_p = p.nprimo
        print('\n P :',str(numero_p))

        q = GeradorNumeroPrimo()
        numero_q = q.nprimo
        print('\n Q :',str(numero_q))

        chaves = Chaves(numero_p, numero_q)
        chaves.geradorchave()

        encripta = chaves.codifica_msg()
        chaves.decodifica_msg(encripta)
    
    elif (opcao == 2 and opcao != 3):

        p=int(input("Digite o Valor P o mesmo deve ser primo:  "))
        q=int(input("\nDigite o Valor Q o mesmo deve ser primo:  "))

        chaves = Chaves(p, q)
        chaves.geradorchave()

        encripta = chaves.codifica_msg()
        chaves.decodifica_msg(encripta)

    elif (opcao == 3):

        print("Fim do Codificador")
        exit

    else:

        print("Opção inexistente, coloque um valor válido!\n")        
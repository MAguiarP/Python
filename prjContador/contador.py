from time import sleep


print("Menu:\n 0 - Sair\n 1 - Contador\n 2 - Contador Regressivo\n")
opcao = input("Informe qual opção você deseja: ")

if opcao =='1':
    tempo = int(input("Quanto tempo você deseja contar?\nR:"))
    for c in range(1, tempo + 1):

listaJogos = []
produtos = ""

while produtos != '0':
    produtos = input("Informe o nome de um jogo para adicioná-lo á lista de jogos ou digite 0 para sair:\n")
    if produtos != '0':
        listaJogos.append(produtos)
    else:
        print("Finalizando...\n")

opcao = input("Deseja exibir a lista de jogos? Digite 's' para sim ou 'n' para não:").lower()
if opcao == 's':
    contagem = 1 
    for jogo in listaJogos:
        print(f"Jogo Número {contagem}:", jogo)
        contagem  = 1
else:
    exit
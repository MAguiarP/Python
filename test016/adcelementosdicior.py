jogos = {1: 'God of War', 2: 'Valorant', 3: 'Far Cry', 4: 'Forza Horizon 5'}

jogos[4] = 'Batman'
print(jogos)

novoJogo = {5: 'The Last of Us'}
jogos.update(novoJogo)
print(jogos)

jogos.update({6: 'Overwatch'})
print(jogos)

jogos.pop(1)
print(jogos)

del jogos[2]
print(jogos)
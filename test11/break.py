for c in range(0, 51):
    if c ==50:

        print(f"Número {c} antingido, saindo..")
        break
    else:
        print(c)

while True:
    parada = int(input("\n Digite 0 para finalizar as iterações do bloco while: "))
    if parada == 0 :
        print("Finalizando...")
        break
    else:
        print("O número digitado não foi 0, retornando....")
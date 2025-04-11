print("Solta a carta, caralho, tigrinho filha da puta.")
musica = input("Qual a próxima frase da música? ")
def musica(musica):
    if musica == "Solta a carta, caralho, tigrinho filha da puta":
            print("Você digitou a primeira opção")
    while True:
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            musica()
        elif escolha == '2':
            print("Você escolheu Informações!")
            # Adicione a lógica para a opção Informações aqui
        elif escolha == '3':
            print("Você escolheu Avançar!")
            # Adicione a lógica para a opção Avançar aqui
        elif escolha == '4':
            print("Você escolheu Voltar!")
            # Adicione a lógica para a opção Voltar aqui
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

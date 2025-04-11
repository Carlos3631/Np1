def verificar_resposta(resposta):
    correta = "Pra eu pegar o meu dinheiro e comer umas quatro puta"
    if resposta.lower() == correta.lower():  # Ignora maiúsculas/minúsculas
        print("Correto! Agora tente a próxima parte da música!")
        print("Tente adivinhar a próxima frase da música.")
    else:
        print("Errado! Tente novamente.")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Pra eu pegar o meu dinheiro e comer umas quatro puta")
        print("2 - Solta a carta, caralho, tigrinho filha da puta")
        print("3 - Pra eu pegar o meu dinheiro e comer umas quatro puta")
        print("4 - É vuk-vuk, vuk, vuk na onda maluca")
        print("5 - É vuk-vuk, vuk, vuk, yeah")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            verificar_resposta(resposta)
        elif escolha == '1':
            print("Pra eu pegar o meu dinheiro e comer umas quatro puta")
        resposta =input("Parabens, você acertou a música! Deseja jogar novamente? (s/n)")
        break
        if resposta.lower() == 's':
                menu()
        elif escolha == '2':
            print("É vuk-vuk, vuk, vuk, yeah")
            errado = input("Tente novamente:")
        elif escolha == '3':
            print("Solta a carta, caralho, tigrinho filha da puta")
            errado = input("Tente novamente:")
        elif escolha == '4':
            print("Pra eu pegar o meu dinheiro e comer umas quatro puta")
            errado = input("Tente novamente:")
        elif escolha == '5':
            print("É vuk-vuk, vuk, vuk na onda maluca")
            errado = input("Tente novamente:")


# Início do jogo
print("Solta a carta, caralho, tigrinho filha da puta.")
menu()

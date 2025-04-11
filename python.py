import random
##--------------------------------------------------------------
##Importando a biblioteca random para gerar números aleatórios.
##Essa biblioteca é útil para criar jogos, simulações e qualquer situação que exija aleatoriedade.
##--------------------------------------------------------------
##Em Python, DEF é usado para definir funções. 
##Uma função é um bloco de código reutilizável que executa uma tarefa específica.
##Para que serve def?
##Organização: Evita código repetitivo.
##Reutilização: Você pode chamar a função quantas vezes quiser.
##Modularidade: Deixa o código mais limpo e fácil de entender.
##--------------------------------------------------------------

def menu():
    print("Bem-vindo ao Hub!")
    print("1. Jogar")
    print("2. Informações")
    print("3. Avançar")
    print("4. Voltar")
    print("5. Sair")

##--------------------------------------------------------------
##O WHILE em Python é usado para criar loops
##ou seja, repetir um bloco de código enquanto uma condição for verdadeira.
##Loop infinito (cuidado! ⚠️)
##Se a condição nunca for falsa, o loop continuará para sempre:
##Usando while para validar entrada do usuário:
##--------------------------------------------------------------
##O IF em Python é usado para fazer verificações e tomar decisões no código.
##Ele executa um bloco de código somente se a condição for verdadeira.
##O ELIF (abreviação de "else if") é usado quando queremos testar múltiplas condições em um if. 
##Ele permite adicionar verificações extras antes de chegar no else
##📌 Importante:
##O elif só é avaliado se o if anterior for falso.
##Assim que uma condição for verdadeira, o resto do código dentro do if é ignorado.
##--------------------------------------------------------------

    while True:
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            submenu_jogar()
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

def submenu_jogar():
    print("Escolha um jogo:")
    print("1. Forca")
    print("2. Adivinha")
    print("3. Voltar")

    while True:
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            jogar_forca()
        elif escolha == '2':
            print("Você escolheu Adivinha!")
            # Adicione a lógica para o jogo Adivinha aqui
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

def jogar_forca():
    print("Você escolheu Forca!")
    palavras_com_dicas = [
        ("Python", "Linguagem de programação"),
        ("Informática", "Área de estudo relacionada a computadores"),
        ("Programação", "Ato de escrever código"),
        ("Faculdade", "Instituição de ensino superior"),
        ("Projeto", "Trabalho desenvolvido para um objetivo específico")
    ]
    palavra, dica = random.choice(palavras_com_dicas)
    palavra = palavra.upper()
    letras_adivinhadas = []
    tentativas = 10

    print(f"Dica: {dica}")

    while tentativas > 0:
        palavra_oculta = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
        print(f"Palavra: {palavra_oculta}")
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Digite uma letra: ").upper()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra.")
        elif letra in palavra:
            letras_adivinhadas.append(letra)
            if all([letra in letras_adivinhadas for letra in palavra]):
                print(f"Parabéns! Você adivinhou a palavra: {palavra}")
                break
        else:
            tentativas -= 1
            print("Letra incorreta.")

        if tentativas == 0:
            print(f"Você perdeu! A palavra era: {palavra}")
            break
if __name__ == "__main__":
    menu()
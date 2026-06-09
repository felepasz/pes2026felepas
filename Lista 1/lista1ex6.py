#6 - Jogo do Pedra, Papel, Tesoura. Solicite as escolhas do jogador 1 e do jogador 2
#(“pedra”, “papel” ou “tesoura”). Use condicionais para determinar quem ganhou:
#• Pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra.
#• Exiba uma mensagem como “Jogador 1 venceu!” ou “Empate!”.

player1 = str(input("Pedra, papel ou tesoura. Digite sua escolha: "))
player2 = str(input("Pedra, papel ou tesoura. Digite sua escolha: "))

if player1 == "pedra" and player2 == "tesoura" :
    print("Player 1 venceu")

if player1 == "tesoura" and player2 == "papel" :
    print("Player 1 venceu")

if player1 == "papel" and player2 == "pedra" :
    print("Player 1 venceu")

if player2 == "pedra" and player1 == "tesoura" :
    print("Player 2 venceu")

if player2 == "tesoura" and player1 == "papel" :
    print("Player 2 venceu")

if player2 == "papel" and player1 == "pedra" :
    print("Player 2 venceu")

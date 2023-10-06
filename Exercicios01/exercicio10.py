import random
def escolhaUsu():
    print("Escolha uma opção:")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    escolha = input("Digite o número correspondente à sua escolha: ")
    return escolha

# Função para obter a escolha aleatória do computador
def escolhaPC():
    escolhas = ["Pedra", "Papel", "Tesoura"]
    escolhaPC = random.choice(escolhas)
    return escolhaPC


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif (user_choice == "1" and computer_choice == "Tesoura") or \
         (user_choice == "2" and computer_choice == "Pedra") or \
         (user_choice == "3" and computer_choice == "Papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"


usuario = escolhaUsu()
if usuario in ["1", "2", "3"]:
        usuario = int(usuario)
        usuario = "Pedra" if usuario == 1 else "Papel" if usuario == 2 else "Tesoura"
        escolhaPC = escolhaPC()
        print(f"Você escolheu: {usuario}")
        print(f"O computador escolheu: {escolhaPC}")
        result = determine_winner(usuario, escolhaPC)
        print(result)
else:
        print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
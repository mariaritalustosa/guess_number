import random

print("Welcome to the Guess the Number Game!")
choice_number = input("Digite o número máximo do jogo: ")

if choice_number.isdigit():
    choice_number = int(choice_number)

else:
    print("Por favor, digite um número válido.")
    quit()


random_number = random.randint(0, choice_number)


while True:
    answer_user = input("Adivinhe o número: ")
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        answer_user = input("Erro: o valor informado não é válido. Tente novamente!")
        continue

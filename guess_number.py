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

import random
import string

def password_generator(len_password = 8):
    letter_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = letter_options + number_options + punt_options

    password_user = ""

    for i in range(0, len_password):
        digit = random.choice(options)
        password_user = password_user + digit

    return password_user

user_choice = input("Quantos digitos na senha?")

if user_choice.isdigit():
    user_choice = int(user_choice)
else:
    print("Entrada inválida!")
    quit()

random_password = password_generator(len_password = user_choice)
print(f"Senha gerada: {random_password}")
#O arquivo em questão cria um arquivo txt para simular uma agenda, que adiciona nome, telefone e email.

#FUNÇÕES

#FUNÇÃO PARA ADICIONAR CONTATO
def adc_contato():
    with open("agenda.txt", "a", encoding="utf-8") as agenda:
        nome = input("Digite o nome do contato para adicionar a agenda\n>>")
        agenda.write('Nome: ' + nome + ';\n')
        email = input("Digite o email\n>>")
        agenda.write('E-mail: ' + email + ';\n')
        tel = input("Digite o telefone\n>>")                                                     
        agenda.write('Telefone: ' + tel + ';\n')
        agenda.write('\n')

#FUNÇÃO QUE LISTA OS CONTATOS DA AGENDA ATUAL
def listar_contatos():
    with open('agenda.txt', 'r', encoding="utf-8") as agenda:
        print(agenda.read())

#FUNÇÃO QUE REINICIA A AGENDA
def reiniciar_agenda():
    with open('agenda.txt', 'w', encoding="utf-8") as agenda:
        adc_contato()

#FUNCIONAMENTO

while True:
    try:   
        opcao = int(input("Digite 1 para criar contato\nDigite 2 para listar os contatos\nDigite 3 para criar uma nova agenda em branco\nDigite 4 para sair. \n>> "))
    except ValueError:
        print('Tipo de dado não válido.')
   
    
    try:    
        if opcao == 1:
            adc_contato()
        
        elif opcao == 2:
            listar_contatos()

        elif opcao == 3:
            print("\nContatos apagados, agenda resetada..\n")
            print("Criando nova agenda...\n")
            reiniciar_agenda()

        elif opcao == 4:
            print("Fechando agenda...")
            break
        
        else:
            print("valor inválido.")
    
    except NameError:
        print('Tipo de dado não válido.')





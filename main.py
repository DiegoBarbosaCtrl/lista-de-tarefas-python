print("---- Bem-vindo ao To Do List ----")
lista_tarefas = []

while True:
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefas")
    print("4. Sair")
    opcao = int(input("Escolha uma opção entre 1 a 4 para prosseguir: "))
    if opcao == 1:
        tarefa = (input("Digite a tarefa para adicionar na lista: "))
        lista_tarefas.append(tarefa)
        
    elif opcao == 2:
        print(lista_tarefas)
        
    elif opcao == 3:
        produto = input("Digite o nome do produto para remover: ")
        if produto in lista_tarefas:
            print("-- Selecione uma tarefa para remover --")
            print(lista_tarefas)
            print("-----------------------------------------")
            lista_tarefas.remove(produto)
            
        else:
            print("Não existe este tarefa na lista. Tente novamente")
    elif opcao == 4:
        print("Obrigado por utilizar nosso To Do List. Até Logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
   
        
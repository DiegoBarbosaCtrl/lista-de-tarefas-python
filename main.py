#Inicio e definição de dados
print("---- Bem-vindo ao To Do List ----")
lista_tarefas = []

#Loop principal da lista
while True:
    #Tela principal para navegar na lista de tarefas
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefas")
    print("4. Sair")
    opcao = int(input("Escolha uma opção entre 1 a 4 para prosseguir: "))
    
    #Primeira opção de adicionar tarefas
    if opcao == 1:
        tarefa = (input("Digite a tarefa para adicionar na lista: "))
        lista_tarefas.append(tarefa)
        
    #Segunda opção para listar tarefas que foram adicionadas até o momento
    elif opcao == 2:
        print("--- Suas Tarefas ---")
        if not lista_tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            for i, tarefa in enumerate(lista_tarefas):
                print(f"{i + 1}. {tarefa}")
        print("----------------------")
            
        #Terceira opção para remover tarefas
    elif opcao == 3:
        if not lista_tarefas:
            print("Nenhuma tarefa para remover")
        else:
            for i, tarefa in enumerate(lista_tarefas):
                print(f"{i + 1}. {tarefa}")
            try:
                numero_para_remover = int(input("Digite o NÚMERO da tarefa que deseja remover: "))
                if 1 <= numero_para_remover <= len(lista_tarefas):
                    indice = numero_para_remover - 1
                    tarefa_removida = lista_tarefas.pop(indice)
                    print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
                else:
                    print("Número inválido! Escolha um número que está na lista")
            except ValueError:
                    print("Entrada invalida. Por favor, digite um número")
                
    #Quarta opção para sair do loop
    elif opcao == 4:
        print("Obrigado por utilizar nosso To Do List. Até Logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
   
        
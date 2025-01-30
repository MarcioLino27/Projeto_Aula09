tarefas = [
    {"Nome": "Lavar a louça", "Descrição": "Lavar e secar a louça de ontem", "Prioridade": 2, "Categoria": "Doméstica", "Concluída": False},
    {"Nome": "Ir para academia", "Descrição": "Malhar peito e tríceps", "Prioridade": 1, "Categoria": "Saúde", "Concluída": False},
    {"Nome": "Estudar py", "Descrição": "Revisar funções e dicionários", "Prioridade": 3, "Categoria": "Educação", "Concluída": False},
    {"Nome": "Caminhar", "Descrição": "Ir até a esquina e voltar", "Prioridade": 1, "Categoria": "Saúde", "Concluída": False}
]

def listar_tarefas(filtrar_prioridade=None):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.\n")
        return
    
    print("\n=== Lista de Tarefas ===")
    for i, tarefa in enumerate(tarefas, start=1):
        if filtrar_prioridade is not None and tarefa["Prioridade"] != filtrar_prioridade:
            continue
        
        status = "Concluída" if tarefa["Concluída"] else "Pendente"
        print(f"\n{i}. {tarefa['Nome']}")
        print(f"   Descrição: {tarefa['Descrição']}")
        print(f"   Prioridade: {tarefa['Prioridade']}")
        print(f"   Categoria: {tarefa['Categoria']}")
        print(f"   Status: {status}")
    print("\n========================\n")

def concluir_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para concluir: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["Concluída"] = True
            print("\nTarefa concluída com sucesso!\n")
        else:
            print("\nNúmero inválido.\n")
    except ValueError:
        print("\nEntrada inválida. Digite um número.\n")

def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição: ")
    try:
        prioridade = int(input("Prioridade (1-Alta, 2-Média, 3-Baixa): "))
    except ValueError:
        print("\nEntrada inválida. Prioridade deve ser um número (1, 2 ou 3).\n")
        return
    categoria = input("Categoria: ")
    
    tarefas.append({"Nome": nome, "Descrição": descricao, "Prioridade": prioridade, "Categoria": categoria, "Concluída": False})
    print("\nTarefa adicionada com sucesso!\n")

def listar_por_prioridade():
    try:
        prioridade = int(input("Digite a prioridade desejada (1-Alta, 2-Média, 3-Baixa): "))
        if prioridade not in [1, 2, 3]:
            print("\nPrioridade inválida. Escolha entre 1, 2 ou 3.\n")
            return
        listar_tarefas(filtrar_prioridade=prioridade)
    except ValueError:
        print("\nEntrada inválida. Digite um número.\n")

def menu():
    while True:
        print("\n1 - Listar Todas as Tarefas\n2 - Listar por Prioridade\n3 - Adicionar Tarefa\n4 - Concluir Tarefa\n5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas()
        elif opcao == "2":
            listar_por_prioridade()
        elif opcao == "3":
            adicionar_tarefa()
        elif opcao == "4":
            concluir_tarefa()
        elif opcao == "5":
            print("\nSaindo...\n")
            break
        else:
            print("\nOpção inválida.\n")

menu()
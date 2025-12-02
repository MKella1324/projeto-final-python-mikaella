clientes = []
proximo_id = 1

def cadastrar():
    global proximo_id
    nome = input("Nome: ").strip()
    tel = input("Telefone: ").strip()
    serv = input("Serviço: ").strip()
    if not nome or not tel:
        print("Erro: Nome e telefone são obrigatórios")
        return
    clientes.append({"id": proximo_id, "nome": nome, "telefone": tel, "servico": serv})
    print(f"Cliente cadastrado! ID: {proximo_id}")
    proximo_id += 1

def listar():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for c in clientes:
        print(f"{c['id']} | {c['nome']} | {c['telefone']} | {c['servico']}")

def atualizar():
    try: idc = int(input("ID do cliente: "))
    except: print("ID inválido"); return
    for c in clientes:
        if c["id"] == idc:
            opt = input("Alterar: 1-Nome 2-Tel 3-Serviço: ")
            if opt=="1": c["nome"]=input("Novo nome: ").strip()
            elif opt=="2": c["telefone"]=input("Novo telefone: ").strip()
            elif opt=="3": c["servico"]=input("Novo serviço: ").strip()
            else: print("Opção inválida"); return
            print("Atualizado!"); return
    print("Cliente não encontrado.")

def remover():
    try: idc=int(input("ID do cliente: "))
    except: print("ID inválido"); return
    for c in clientes:
        if c["id"]==idc:
            clientes.remove(c)
            print("Cliente removido!"); return
    print("Cliente não encontrado.")

def relatorio():
    print(f"Total: {len(clientes)}")
    cont = {}
    for c in clientes:
        cont[c['servico']] = cont.get(c['servico'],0)+1
    for s,q in cont.items():
        print(f"{s}: {q} cliente(s)")

def menu():
    while True:
        print("\n1-Cadastrar 2-Listar 3-Atualizar 4-Remover 5-Relatório 6-Sair")
        op = input("Escolha: ")
        if op=="1": cadastrar()
        elif op=="2": listar()
        elif op=="3": atualizar()
        elif op=="4": remover()
        elif op=="5": relatorio()
        elif op=="6": break
        else: print("Inválido!")

menu()
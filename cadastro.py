def cadastrar_nome(cadastro):
     novo_nome = input("Digite o nome da pessoa: ")
     cadastro.append(novo_nome)
     print(f"Usuário {novo_nome} foi adicionado com sucesso")

def listar_nome(cadastro):
    print("\nLista de nomes cadastrados: ")
    for i, nome in enumerate(cadastro, start=1):
        print(f"{i}. {nome}")

def excluir_nome(cadastro):
     excluir_nome = input("Digite o nome para excluir: ")
     if excluir_nome in cadastro:
         cadastro.remove(excluir_nome)
         print(f"{excluir_nome} foi removido.")
     
def menu():
    cadastro = []
    while True:
        print("\n----- Cadastro e funcionários-----")
        print("[1] Cadastrar Pessoa ")
        print("[2] Listar Pessoas ")
        print("[3] Excluir pessoa")
        print("[0] ")
        opção = input("Escolha uma opção: ")

        if opção == '1':
            cadastrar_nome(cadastro)
        elif opção == '2':
            listar_nome(cadastro)
        elif opção == '3':
            excluir_nome(cadastro)
        elif opção== '0':
            print("Saindo...")
            break
        else:
            print("!!! Opção invalida. Tente novamente. !!!")
menu()
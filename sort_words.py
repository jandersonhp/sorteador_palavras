import random

## tentando lembrar como escrevi a primeira versão do código
## todo: opt 2 remover palavra por item (index -1)
## todo: opt 4 mostrar lista e sortear
## todo: opt 5 perguntar qntas palavras sortear
## separar em funções e depois refatorar código

lista = []

# Menu interativo
while True:
    print("Menu".center(20, "="))
    print("""1- Adicionar Palavra
2- Remover Palavra
3- Listar Palavras
4- Sortear Uma Palavra
5- Sortear Duas Palavras
6- Limpar Lista
7- Sair""")
    
    try:
        opcao = int(input("Escolha uma opção do menu: "))
    except ValueError:
        print("Opção inválida. Escolha apenas números.\n")
        continue

# Opções escolhidas
    if opcao == 1:
        palavra = input("Digite a palavra: ")
        lista.append(palavra)
        print(f"Palavra '{palavra}' adicionada!\n")

    elif opcao == 2:
        remover = input("Qual palavra deseja remover? ")
        if remover in lista:
            lista.remove(remover)
            print("Palavra removida.\n")
        else:
            print("Palavra não encontrada.\n")

    elif opcao == 3:
        if lista:
            print("\nPalavras".center(20,"="))
            for w, palavra in enumerate(lista, start=1):
                print(f"{w} - {palavra}")
                print()
        else:
            print("Lista vazia. Adicione pelo menos uma palavra!\n")

    elif opcao == 4:
        if lista:
            print("Palavra sorteada:", random.choice(lista), "\n")
        else:
            print("Lista vazia, não há o que sortear.\n")

    elif opcao == 5:
        if len(lista) >= 2:
            sorteadas = random.sample(lista, 2)
            print("Palavras sorteadas:", sorteadas, "\n")
        else:
            print("É preciso pelo menos duas palavras.\n")

    elif opcao == 6:
        try:
            confirmar = int(input('''Tem certeza que deseja excluir todas as palavras da lista?
1- Sim.
2- Não.
Opção nº: '''))
            if confirmar == 1:
                lista.clear()
                print("Lista esvaziada, palavras excluídas!\n")
            elif confirmar == 2:
                print("Lista não esvaziada. Palavras mantidas.\n")
            else:
                print("Escolha inválida.\n")
        except ValueError:
            print("Opção inválida. Escolha apenas o número da opção.\n")

    elif opcao == 7:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida.\n")

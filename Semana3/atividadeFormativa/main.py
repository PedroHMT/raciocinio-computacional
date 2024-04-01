op = -1
while op != 0:
    try:
        print("* Menu Principal *")
        print("1 - Gerenciamento de Estudantes")
        print("2 - Gerenciamento de Disciplinas")
        print("3 - Gereciamento de Professores")
        print("4 - Gerenciamento de Turmas")
        print("5 - Gerenciamento de Matriculas")
        print("0 - Sair")

        op = int(input("\nInsira o número da Opção desejada: "))
        opp = -1
        print("")

        # Estudantes
        if op == 1:
            while opp != 0:
                try:
                    print("* Menu de Operações *")
                    print("1 - Incluir")
                    print("2 - Listar")
                    print("3 - Atualizar")
                    print("4 - Excluir")
                    print('0 - Retornar ao Menu Principal')
                    opp = int(input("\nInsira o número da Opção desejada: "))
                    if opp == 1:
                        print("\n== Inserir Estudantes ==\n")
                    elif opp == 2:
                        print("\n== Listar Estudantes ==\n")
                    elif opp == 3:
                        print("\n== Atualizar Estudantes ==\n")
                    elif opp == 4:
                        print("\n== Excluir Estudantes ==\n")
                    elif opp == 0:
                        print("\n== Retornando ao Menu Principal ==\n")
                    else:
                        print("\nOpção Inválida\n")
                except ValueError:
                    print("\nOpção Inválida\n")
        # Disciplinas
        elif op == 2:
            while opp != 0:
                try:
                    print("1 - Incluir")
                    print("2 - Listar")
                    print("3 - Atualizar")
                    print("4 - Excluir")
                    print('0 - Retornar ao Menu Principal')
                    opp = int(input("\nInsira o número da Opção desejada: "))
                    if opp == 1:
                        print("\n== Inserir Disciplinas ==\n")
                    elif opp == 2:
                        print("\n== Listar Disciplinas ==\n")
                    elif opp == 3:
                        print("\n== Atualizar Disciplinas ==\n")
                    elif opp == 4:
                        print("\n== Excluir Disciplinas ==\n")
                    elif opp == 0:
                        print("\n== Retornando ao Menu Principal ==\n")
                    else:
                        print("\nOpção Inválida\n")
                except ValueError:
                    print("\nOpção Inválida\n")

        # Professores
        elif op == 3:
            while opp != 0:
                try:
                    print("1 - Incluir")
                    print("2 - Listar")
                    print("3 - Atualizar")
                    print("4 - Excluir")
                    print('0 - Retornar ao Menu Principal')
                    opp = int(input("\nInsira o número da Opção desejada: "))
                    if opp == 1:
                        print("\n== Inserir Professores ==\n")
                    elif opp == 2:
                        print("\n== Listar Professores ==\n")
                    elif opp == 3:
                        print("\n== Atualizar Professores ==\n")
                    elif opp == 4:
                        print("\n== Excluir Professores ==\n")
                    elif opp == 0:
                        print("\n== Retornando ao Menu Principal ==\n")
                    else:
                        print("\nOpção Inválida\n")
                except ValueError:
                    print("\nOpção Inválida\n")

        # Turmas
        elif op == 4:
            while opp != 0:
                try:
                    print("1 - Incluir")
                    print("2 - Listar")
                    print("3 - Atualizar")
                    print("4 - Excluir")
                    print('0 - Retornar ao Menu Principal')
                    opp = int(input("\nInsira o número da Opção desejada: "))
                    if opp == 1:
                        print("\n== Inserir Turmas ==\n")
                    elif opp == 2:
                        print("\n== Listar Turmas ==\n")
                    elif opp == 3:
                        print("\n== Atualizar Turmas ==\n")
                    elif opp == 4:
                        print("\n== Excluir Turmas ==\n")
                    elif opp == 0:
                        print("\n== Retornando ao Menu Principal ==\n")
                    else:
                        print("\nOpção Inválida\n")
                except ValueError:
                    print("\nOpção Inválida\n")

        # Matriculas
        elif op == 5:
            while opp != 0:
                try:
                    print("1 - Incluir")
                    print("2 - Listar")
                    print("3 - Atualizar")
                    print("4 - Excluir")
                    print('0 - Retornar ao Menu Principal')
                    opp = int(input("\nInsira o número da Opção desejada: "))
                    if opp == 1:
                        print("\n== Inserir Matriculas ==\n")
                    elif opp == 2:
                        print("\n== Listar Matriculas ==\n")
                    elif opp == 3:
                        print("\n== Atualizar Matriculas ==\n")
                    elif opp == 4:
                        print("\n== Excluir Matriculas ==\n")
                    elif opp == 0:
                        print("\n== Retornando ao Menu Principal ==\n")
                    else:
                        print("\nOpção Inválida\n")
                except ValueError:
                    print("\nOpção Inválida\n")
        elif op == 0:
            print("\n== Finalizando Aplicativo ==\n")
        else:
            print("\nOpção Inválida\n")
    except ValueError:
        print("\nOpção Inválida\n")
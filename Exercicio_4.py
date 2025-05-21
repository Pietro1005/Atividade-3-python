def menu():
    while True:
        print("Escolha uma opção:")
        print("[1] Olá")
        print("[2] Ajuda")
        print("[3] Sair")
        
        escolha = input("Digite o número da opção: ")
        
        if escolha == '1':
            print("Olá! Como você está?")
        elif escolha == '2':
            print("Este é um menu simples. Escolha uma opção para interagir.")
        elif escolha == '3':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha novamente.")

menu()

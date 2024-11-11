from models.functions import *
player1 = input("Digite o nome do jogador 1: ")
print("Você será o X")
player2 = input("Digite o nome do jogador 2: ")
print("Você será o O")

gameboard = create_matrix() 
gui_gameboard = create_gui_matrix()

i = 0
for i in range(9):
    print("-"*50)
    
    if i % 2 == 0: 
        print(f'{player2}, sua vez: ')
        
        gui_gameboard_pass = update_gui_matrix(gameboard, gui_gameboard)
        gui_gameboard = gui_gameboard_pass
        show_gui_gameboard(gui_gameboard)

        choice_line = int(input("Digite a linha onde desaja marcar: "))
        choice_col = int(input("Digite a coluna onde deseja marcar: "))
        

        while is_marked(choice_line, choice_col, gameboard) or out_of_index(choice_line, choice_col):
            print("-"*50)
            print(f'Linha {choice_line} e coluna {choice_col} já estão ocupados ou estão fora do tamanho da matriz \nEscolha outra posição!!!')
            print("")
            choice_line = int(input("Digite a linha onde deseja marcar: "))
            choice_col = int(input("Digite a coluna onde deseja marcar: "))

        gameboard_pass = mark_matrix(choice_line, choice_col, gameboard, 2)
        gameboard = gameboard_pass
        condition = win_condition(gameboard)
        if condition != 0:
            if condition == 1:
                print("-"*33)
                print(f"| PARABÉNS {player1}, VOCÊ GANHOU!!! |")
                print("-"*33)
                break
            else:
                print("-"*33)
                print(f"| PARABÉNS {player2}, VOCÊ GANHOU!!! |")
                print("-"*33)
                break
        

    else:#jogador 1
        print(f'{player1}, sua vez: ')

        gui_gameboard_pass = update_gui_matrix(gameboard, gui_gameboard)
        gui_gameboard = gui_gameboard_pass
        show_gui_gameboard(gui_gameboard)

        choice_line = int(input("Digite a linha onde desaja marcar: "))
        choice_col = int(input("Digite a coluna onde deseja marcar: "))

        while is_marked(choice_line, choice_col, gameboard) or out_of_index(choice_line, choice_col):
            print("-"*50)
            print(f'Linha {choice_line} e coluna {choice_col} já estão ocupados ou estão fora do tamanho da matriz \nEscolha outra posição!!!')
            print()
            choice_line = int(input("Digite a linha onde deseja marcar: "))
            choice_col = int(input("Digite a coluna onde deseja marcar: "))
            
        gameboard_pass = mark_matrix(choice_line, choice_col, gameboard, 1)
        gameboard = gameboard_pass
        condition = win_condition(gameboard)
        if condition != 0:
            if condition == 1:
                print("-"*33)
                print(f"| PARABÉNS {player1}, VOCÊ GANHOU!!! |")
                print("-"*33)
                break
            else:
                print("-"*33)
                print(f"| PARABÉNS {player2}, VOCÊ GANHOU!!! |")
                print("-"*33)
                break

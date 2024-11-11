def create_matrix():
    matrix = []
    for i in range(3):
        line = []
        for i in range(3):
            line.append(0)
        matrix.append(line)
    return matrix

def mark_matrix(line, col, gameboard, player):
    gameboard[line][col] = player
    return gameboard

def is_marked(line, col, gameboard):
    try:
        if gameboard[line][col] != 0:
            return True
    except:
            return False

def win_condition(gameboard):

    for i in range(3):
        if gameboard[i][0] == gameboard[i][1] == gameboard[i][2] and gameboard[i][0] != 0:
            return gameboard[i][0]  

    for i in range(3):
        if gameboard[0][i] == gameboard[1][i] == gameboard[2][i] and gameboard[0][i] != 0:
            return gameboard[0][i]  

    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] and gameboard[0][0] != 0:
        return gameboard[0][0] 

    if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] and gameboard[0][2] != 0:
        return gameboard[0][2]  

    return 0

def create_gui_matrix():
    matrix = []
    for i in range(3):
        line = []
        for j in range(3):
            line.append("-")
        matrix.append(line)
    return matrix
            
def update_gui_matrix(gameboard, gui_gameboard):
    for i in range(3):
        for j in range(3):
            if gameboard[i][j] == 1:
                gui_gameboard[i][j] = "X"
            if gameboard[i][j] == 2:
                gui_gameboard[i][j] = "O"
    return gui_gameboard

def show_gui_gameboard(gui_gameboard):
    print("\t0\t1\t2")

    print("")
    for i in range(3):
        print(i, end='\t')
        for j in range(3):
            print(gui_gameboard[i][j], end='\t')
        print("\n")
    print("\n")

def out_of_index(line, col):
    if line < 0 or line > 2:
        return True
    elif col < 0 or col > 2:
        return True
    else:
        return False
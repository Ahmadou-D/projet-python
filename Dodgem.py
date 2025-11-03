def newBoard(n):
    board = []
    i = 0
    while i < n:
        ligne = []
        j = 0
        while j < n:
            ligne.append(0)
            j = j + 1
        board.append(ligne)
        i = i + 1

    j = 1
    while j < n:
        board[n - 1][j] = 1
        j = j + 1

    i = 0
    while i < n - 1:
        board[i][0] = 2
        i = i + 1

    return board

def displayBoard(board, n):
    i = 0
    while i < n:
        print(i + 1, "|", end=" ")
        j = 0
        while j < n:
            if board[i][j] == 0:
                print(".", end=" ")
            elif board[i][j] == 1:
                print("x", end=" ")
            else:
                print("o", end=" ")
            j = j + 1
        print()
        i = i + 1
    print("  " + "--" * n)
    print("   ", end="")
    k = 0
    while k < n:
        print(k + 1, end=" ")
        k = k + 1
    print()

def possiblePawn(board, n, player, i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if board[i][j] != player:
        return False

    if player == 1:
        if i > 0 and board[i - 1][j] == 0:
            return True
        if j > 0 and board[i][j - 1] == 0:
            return True
        if j < n - 1 and board[i][j + 1] == 0:
            return True
        if i == 0:
            return True
    else:
        if i > 0 and board[i - 1][j] == 0:
            return True
        if j < n - 1 and board[i][j + 1] == 0:
            return True
        if i < n - 1 and board[i + 1][j] == 0:
            return True
        if j == n - 1:
            return True

    return False

def selectPawn(board, n, player):
    while True:
        ligne = input("Joueur " + str(player) + ", choisir la ligne d’un pion : ")
        colonne = input("Joueur " + str(player) + ", choisir la colonne d’un pion : ")

        if ligne.isdigit() == False or colonne.isdigit() == False:
            print("Merci de saisir un nombre.")
            continue

        i = int(ligne) - 1
        j = int(colonne) - 1

        if possiblePawn(board, n, player, i, j):
            return i, j
        else:
            print("Ce pion ne peut pas être déplacé.")

def possibleMove(board, n, player, i, j, direction):
    if player == 1:
        if direction == 1 and i == 0:
            return True  
        if direction == 1 and board[i - 1][j] == 0:
            return True
        if direction == 4 and j > 0 and board[i][j - 1] == 0:
            return True
        if direction == 2 and j < n - 1 and board[i][j + 1] == 0:
            return True
    else:
        if direction == 2 and j == n - 1:
            return True  
        if direction == 1 and i > 0 and board[i - 1][j] == 0:
            return True
        if direction == 2 and j < n - 1 and board[i][j + 1] == 0:
            return True
        if direction == 3 and i < n - 1 and board[i + 1][j] == 0:
            return True
    return False


def selectMove(board, n, player, i, j):
    while True:
        direction = input("Choisir la direction (1 = Nord, 2 = Est, 3 = Sud, 4 = Ouest) : ")
        if direction.isdigit() == False:
            print("Merci de saisir un nombre.")
            continue

        direction = int(direction)
        if direction < 1 or direction > 4:
            print("Direction invalide.")
            continue

        if possibleMove(board, n, player, i, j, direction):
            return direction
        else:
            print("Déplacement impossible.")


def move(board, n, player, i, j, direction):
    board[i][j] = 0

    if player == 1:
        if direction == 1:
            if i == 0:
                return  
            board[i - 1][j] = 1
        elif direction == 2:
            board[i][j + 1] = 1
        elif direction == 4:
            board[i][j - 1] = 1
    else:
        if direction == 2:
            if j == n - 1:
                return  
            board[i][j + 1] = 2
        elif direction == 1:
            board[i - 1][j] = 2
        elif direction == 3:
            board[i + 1][j] = 2

def win(board, n, player):
    i = 0
    while i < n:
        j = 0
        while j < n:
            if board[i][j] == player:
                if possiblePawn(board, n, player, i, j):
                    return False
            j = j + 1
        i = i + 1
    return True

def dodgem(n):
    board = newBoard(n)
    player = 1

    while True:
        displayBoard(board, n)

        if win(board, n, player):
            if player == 1:
                print("Vainqueur : 2")
            else:
                print("Vainqueur : 1")
            break

        print("Au joueur", player, "de jouer.")
        i, j = selectPawn(board, n, player)
        direction = selectMove(board, n, player, i, j)
        move(board, n, player, i, j, direction)

        if player == 1:
            player = 2
        else:
            player = 1


taille = int(input("Choisir la taille du plateau : "))
dodgem(taille)

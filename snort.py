def newBoard(n):
    board = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(0)
        board.append(ligne)
    return board

def displayBoard(board, n):
    for i in range(n):
        print(i+1, "|", end=" ")
        for j in range(n):
            if board[i][j] == 0:
                print(".", end=" ")
            elif board[i][j] == 1:
                print("x", end=" ")
            else:
                print("o", end=" ")
        print() 
    print("  " + "--" * n)

    print("   ", end="")
    for k in range(n):
        print(k+1, end=" ")
    print()  

def possibleSquare(board, n, player, i, j):
    if i < 0:
        return False
    if i >= n:
        return False
    if j < 0:
        return False
    if j >= n:
        return False

    if board[i][j] != 0:
        return False

    if player == 1:
        adversaire = 2
    else:
        adversaire = 1

    if i > 0:
        if board[i-1][j] == adversaire:
            return False
    if i < n-1:
        if board[i+1][j] == adversaire:
            return False
    if j > 0:
        if board[i][j-1] == adversaire:
            return False
    if j < n-1:
        if board[i][j+1] == adversaire:
            return False

    return True

def selectSquare(board, n, player):
    while True:
        ligne = input("Joueur " + str(player) + ", choisir une ligne (1-" + str(n) + ") : ")
        colonne = input("Joueur " + str(player) + ", choisir une colonne (1-" + str(n) + ") : ")

        if ligne.isdigit() == False or colonne.isdigit() == False:
            print("Merci de saisir un nombre.")
            continue

        i = int(ligne) - 1
        j = int(colonne) - 1

        if possibleSquare(board, n, player, i, j):
            return i, j
        else:
            print("Case invalide, réessayez.")

def updateBoard(board, player, i, j):
    board[i][j] = player

def again(board, n, player):
    i = 0
    while i < n:
        j = 0
        while j < n:
            if possibleSquare(board, n, player, i, j):
                return True
            j = j + 1
        i = i + 1
    return False

def snort(n):
    board = newBoard(n)
    player = 1

    while True:
        displayBoard(board, n)

        if again(board, n, player) == False:
            if player == 1:
                print("Vainqueur : 2")
            else:
                print("Vainqueur : 1")
            break

        i, j = selectSquare(board, n, player)
        updateBoard(board, player, i, j)

        if player == 1:
            player = 2
        else:
            player = 1

taille = int(input("Choisir la taille du plateau : "))
snort(taille)

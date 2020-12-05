def filtrado(tupla):
    return tupla[0] == 1

def verificar(i,j, board):
    color = board[i][j]
    color = 1 if color ==2 else 2
    if (board[i-1][j] == color and board[i][j-1] == color and board[i+1][j-1] == color and 
        board[i+1][j] == color and board[i][j+1] == color and board[i-1][j+1] == color):
        return 1
    else:
        return 0

def verificar_encierro(board):
    lista = [(verificar(i,j,board),(i,j))  for i in range(1,6) for j in range(1, 6) if board[i][j] != 0]
    return list(filter(filtrado, lista))
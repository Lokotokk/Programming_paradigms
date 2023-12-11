# Крестики-нолики
# ● Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

board = [1, 2, 3,
         4, 5, 6,
         7, 8, 8]

victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 1[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]        

def print_board():
    print(board[0], end = " ")
    print(board[1], end = " ")
    print(board[2])

    print(board[3], end = " ")
    print(board[4], end = " ")
    print(board[5])

    print(board[6], end = " ")
    print(board[7], end = " ")
    print(board[8])

def step_board(step, symbol):
    ind = board.index(step)
    board[ind] = symbol

def get_result():
    win = ""

    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
             win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O": 
            win = "X"

    return win

game_over = False
player_1 = True

while game_over == False:

    print_board()

    if player_1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "0"
        step = int(input("Игрок 1, ваш ход: "))    

    step_board(step, symbol)
    win = get_result()
    
    if win != "":
        game_over = True
    else:
        game_over = False

    player_1 = not(player_1)          

print_board()
print("Победил", win)
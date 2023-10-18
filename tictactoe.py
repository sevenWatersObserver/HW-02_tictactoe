# изначальные данные
# помещаем поле, ссылки/переводы ввода, внутренний счёт хода,
# номер хода, счёт победы и метка игрока
# Крестик всегда первый
# import os чтобы можно было поставить паузу через os.system('pause')
import os
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
RowsRef, ColumnsRef = ("1", "2", "3"), ("а", "б", "в")
RowsTurn, ColumnsTurn = None, None
moveCount, isWon, playerRep = 0, False, "X"

# функция, которая показывает поле
# работает в начале и после каждого ввода хода
# очень ленивый метод
# поле должно выглядеть так в начале
#
#   а б в
# 1 - - -
# 2 - - -
# 3 - - -


def boardprint():
    print("  а б в")
    row_iter = 1
    for row in board:
        print(row_iter, *row)
        row_iter += 1


# тело программы
boardprint()
print("\n")
print("Крестики-нолики, от Б. by sevenWatersObserver, 18/10/2023, v.1.0")
print('Вводите ход в виде буквы-цифры, например "б2". Первый игрок - крестик.')
# игра начинается
# катим цикл только 9 раз максимум, потому что 9 ячеек
while moveCount < 9:
    # ввод хода
    turnInput = input("Ходит игрок %s:" % playerRep)
    # проверяем правильность ввода и переводим ввод во внутренние данные
    if (len(turnInput) == 2) and (turnInput[0] in ColumnsRef) and (turnInput[1] in RowsRef):
        ColumnsTurn = ColumnsRef.index(turnInput[0])
        RowsTurn = RowsRef.index(turnInput[1])
    else:
        print("Ход введён неправильно, попробуйте ещё раз.")
        continue

    # проверяем ячейку на пустоту, заполняем если пусто
    if board[RowsTurn][ColumnsTurn] == "-":
        board[RowsTurn][ColumnsTurn] = playerRep
    else:
        print("Тут уже походили, попробуйте ещё раз.")
        continue

    boardprint()
    # ищем победу на поле
    # очень ленивый метод, пользуется фактом что поле 3 на 3
    # горизонтальная проверка
    if not isWon:
        for i in range(0, 3):
            if board[RowsTurn][i] != playerRep:
                break
            if i == 2:
                isWon = True
    # вертикальная проверка
    if not isWon:
        for i in range(0, 3):
            if board[i][ColumnsTurn] != playerRep:
                break
            if i == 2:
                isWon = True
    # диагональная проверка 1
    if not isWon:
        for i in range(0, 3):
            if board[i][i] != playerRep:
                break
            if i == 2:
                isWon = True
    # диагональная проверка 2
    if not isWon:
        for i in range(0, 3):
            if board[2-i][i] != playerRep:
                break
            if i == 2:
                isWon = True

    # либо выиграли, либо продолжаем до конца
    if isWon:
        print("Игрок %s победил!" % playerRep)
        break
    else:
        moveCount += 1
        if playerRep == "X":
            playerRep = "O"
        else:
            playerRep = "X"
# пишем, что игра окончена
# если ничья, игра не напишет победителя
print("Игра окончена.")
os.system('pause')

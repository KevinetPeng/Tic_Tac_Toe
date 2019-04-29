# import tkinter GUI library
from tkinter import *
import random

button_val = [[0 for x in range(3)] for y in range(3)]
button_list = []
turn_count = 1

p_one_score, p_two_score = 0, 0

scoreText = 'Score: ' + str(p_one_score) + ' - ' + str(p_two_score)

print(" The losing player will go first. \n If the game is tied, then the starting player is assigned randomly.")


def check_winner():

    for row in range(3):

        dia_counter, diab_counter = 0, 0
        counter = 0
        for index_r in range(3):
            if button_val[index_r][index_r] == 1:
                dia_counter += 1
            if button_val[2-index_r][index_r] == 1:
                diab_counter += 1
            if button_val[index_r][row] == 1:
                counter += 1

        if counter == 3 or dia_counter == 3 or diab_counter == 3 or button_val[row][:].count(1) == 3:
            return 1

        dia_counter, diab_counter = 0, 0
        counter = 0
        for index_r in range(3):
            if button_val[index_r][index_r] == 2:
                dia_counter += 1
            if button_val[2-index_r][index_r] == 2:
                diab_counter += 1
            if button_val[index_r][row] == 2:
                counter += 1

        if counter == 3 or dia_counter == 3 or diab_counter == 3 or button_val[row][:].count(2) == 3:
            return 2

    return 0


def highlight_winner(winner_num):

    for row in range(3):
        if button_val[row][:].count(winner_num) == 3:
            for index in range(3):
                button_list[row*3 + index].configure(bg='#ccffcc')

            return 0

    for col in range(3):
        counter = 0
        for row in range(3):
            if button_val[row][col] == winner_num:
                counter += 1

        if counter == 3:
            for index in range(col, col + 9, 3):
                button_list[index].configure(bg='#ccffcc')
            return 0

    dia_counter, diab_counter = 0, 0
    for index_r in range(3):
        if button_val[index_r][index_r] == winner_num:
            dia_counter += 1
        if button_val[2 - index_r][index_r] == winner_num:
            diab_counter += 1

    if dia_counter == 3:
        for index in range(0, 12, 4):
            button_list[index].configure(bg='#ccffcc')
        return 0

    if diab_counter == 3:
        for index in range(2, 8, 2):
            button_list[index].configure(bg='#ccffcc')
        return 0

    return 0


def onbuttonpress(num1, num2, button_arg, index_arg):
    global turn_count
    global p_one_score
    global p_two_score
    global scoreText

    if turn_count == 1:
        button_arg[num1][num2] = 1
        turn_count = 2

        button_list[index_arg].configure(state="disabled", text="X")

        if check_winner() == 1:
            for index in range(9):
                button_list[index].configure(state="disabled")
            print('Game over: Player 1 wins.')

            highlight_winner(1)
            p_one_score += 1

            scoreText = 'Score: ' + str(p_one_score) + ' - ' + str(p_two_score)
            scoreboard.configure(text=scoreText)

            againButton.configure(bg="#e6fff5")

        else:
            turn_counter.configure(text="P2")

    else:
        button_arg[num1][num2] = 2
        turn_count = 1

        button_list[index_arg].configure(state="disabled", text="O")

        if check_winner() == 2:
            for index in range(9):
                button_list[index].configure(state="disabled")
            print('Game over: Player 2 wins.')

            highlight_winner(2)
            p_two_score += 1

            scoreText = 'Score: ' + str(p_one_score) + ' - ' + str(p_two_score)
            scoreboard.configure(text=scoreText)

            againButton.configure(bg="#e6fff5")

        else:
            turn_counter.configure(text="P1")


def reset(button_arg, color):
    global turn_count
    global p_one_score
    global p_two_score

    for row in range(3):
        for col in range(3):
            button_arg[row][col] = 0

    for index in range(9):
        button_list[index].configure(state="active", text=" ", background=color)

    againButton.configure(bg=color)

    print("Game reset.")

    if p_one_score > p_two_score:
        turn_count = 2
        turn_counter.configure(text="P2")
    elif p_one_score < p_two_score:
        turn_count = 1
        turn_counter.configure(text="P1")

    elif p_one_score == p_two_score:
        turn_count = random.randint(1, 2)

        if turn_count == 1:
            turn_counter.configure(text="P1")
        else:
            turn_counter.configure(text="P2")


# make a root window (primary startup window)
root_window = Tk()
root_window.title("Tic Tac Toe Game")

button00 = Button(root_window, text=" ", font='Arial 50 bold', height=2, width=5, command=lambda: onbuttonpress(
    num1=0, num2=0, button_arg=button_val, index_arg=0), bd=2)
button00.grid(row=1, column=0, sticky=S+N+E+W)
button_list.append(button00)

button01 = Button(root_window, text=" ", font='Arial 50 bold', height=2, width=5, command=lambda: onbuttonpress(
    num1=0, num2=1, button_arg=button_val, index_arg=1), bd=2)
button01.grid(row=1, column=1, sticky=S+N+E+W)
button_list.append(button01)

button02 = Button(root_window, text=" ", font='Arial 50 bold', height=2, width=5, command=lambda: onbuttonpress(
    num1=0, num2=2, button_arg=button_val, index_arg=2), bd=2)
button02.grid(row=1, column=2, sticky=S+N+E+W)
button_list.append(button02)

button10 = Button(root_window, text=" ", font='Arial 50 bold', height=2, width=5, command=lambda: onbuttonpress(
    num1=1, num2=0, button_arg=button_val, index_arg=3), bd=2)
button10.grid(row=2, column=0, sticky=S+N+E+W)
button_list.append(button10)

button11 = Button(root_window, text=" ", font='Arial 50 bold', height=2, width=5, command=lambda: onbuttonpress(
    num1=1, num2=1, button_arg=button_val, index_arg=4), bd=2)
button11.grid(row=2, column=1, sticky=S+N+E+W)
button_list.append(button11)

button12 = Button(root_window, text=" ", font='Arial 50 bold', height=2, width=5, command=lambda: onbuttonpress(
    num1=1, num2=2, button_arg=button_val, index_arg=5), bd=2)
button12.grid(row=2, column=2, sticky=S+N+E+W)
button_list.append(button12)

button20 = Button(root_window, text=" ", font='Arial 50 bold', height=2, width=5, command=lambda: onbuttonpress(
    num1=2, num2=0, button_arg=button_val, index_arg=6), bd=2)
button20.grid(row=3, column=0, sticky=S+N+E+W)
button_list.append(button20)

button21 = Button(root_window, text=" ", font='Arial 50 bold', height=2, width=5, command=lambda: onbuttonpress(
    num1=2, num2=1, button_arg=button_val, index_arg=7), bd=2)
button21.grid(row=3, column=1, sticky=S+N+E+W)
button_list.append(button21)

button22 = Button(root_window, text=" ", font='Arial 50 bold', height=2, width=5, command=lambda: onbuttonpress(
    num1=2, num2=2, button_arg=button_val, index_arg=8), bd=2)
button22.grid(row=3, column=2, sticky=S+N+E+W)
button_list.append(button22)

scoreboard = Label(root_window, text=scoreText, font='Arial 22', height=1, width=10, borderwidth=2, relief="groove")
scoreboard.grid(row=0, column=1, sticky=S+N+E+W)

againButton = Button(root_window, text="Next Round", font="Arial 22", command=lambda: reset(button_arg=button_val,
                     color=orig_color), bd=2)
againButton.grid(row=0, column=2, sticky=S+N+E+W)

orig_color = button_list[1].cget("background")

turn_counter = Label(root_window, text="P1", font='Arial 22', height=1, width=10, borderwidth=2, relief="groove")
turn_counter.grid(row=0, column=0, sticky=S+N+E+W)

root_window.mainloop()
# tell computer to loop the window (and not close it instantly)

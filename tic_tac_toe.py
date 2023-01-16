from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('Tic-Tac-Toe')

# Player1 = 'X'
# stop_game = False
#
# def clicked(r,c):
#     global Player1
#     if Player1 == "X" and states[r] == 0 and stop_game == False:
#         b[r].configure(text = "X")
#         states[r] = 'X'
#         Player1='O'
#
#
#     if Player1 == 'O' and states[r] == 0 and stop_game == False:
#         b[r].configure(text = 'O')
#         states[r] = "O"
#         Player1 = "X"
#
#     check_if_win()
#
#
# def check_if_win():
#     global stop_game
#
#     for i in range(3):
#         if states[i][0] == states[i][1] == states[i][2] !=0:
#             stop_game = True
#             winner = messagebox.showinfo("Winner", states[i][0] + " Won")
#             break
#
#         elif states [0][i] == states[1][i] == states[2][i] != 0:
#             stop_game = True
#             winner = messagebox.showinfo("Winner", states[0][i]+ " Won!")
#             break
#
#         elif states[0][0] == states[1][1] == states[2][2] !=0:
#             stop_game = True
#             winner = messagebox.showinfo("Winner", states[0][0]+ " Won!")
#             break
#
#         elif states[0][2] == states[1][1] == states[2][0] !=0:
#             stop_game = True
#             winner = messagebox.showinfo("Winner" , states[0][2]+ " Won!")
#             break
#
#         elif states[0][0] and states[0][1] and states[0][2] and states[1][0] and states[1][1] and states[1][2] and states[2][0] and states[2][1] and states[2][2] != 0:
#             stop_game = True
#             winner = messagebox.showinfo("tie", "Tie")
#
#
#
#
#
#
#
#
#
#
#
# root.geometry('450x520')
#
# root.resizable(0,0)
#
# #Button
# b = [
#      [0,0,0],
#      [0,0,0],
#      [0,0,0]]
#
# #text for buttons
# states = [
#      [0,0,0],
#      [0,0,0],
#      [0,0,0]]
#
# for i in range(3):
#     for j in range(3):
#
#         b[i][j] = Button(
#                         height = 4, width = 8,
#                         font = ("Helvetica","20"),
#                         command = lambda r = i, c = j : clicked(r,c))
#         b[i][j].grid(row = i, column = j)


def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

def checkifwon():
	global winner
	winner = False

	if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
		b1.config(bg="red")
		b2.config(bg="red")
		b3.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()
	elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
		b4.config(bg="red")
		b5.config(bg="red")
		b6.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
		b7.config(bg="red")
		b8.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
		b1.config(bg="red")
		b4.config(bg="red")
		b7.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
		b2.config(bg="red")
		b5.config(bg="red")
		b8.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
		b3.config(bg="red")
		b6.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
		b1.config(bg="red")
		b5.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
		b3.config(bg="red")
		b5.config(bg="red")
		b7.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()

	#### CHECK FOR O's Win
	elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
		b1.config(bg="red")
		b2.config(bg="red")
		b3.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()
	elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
		b4.config(bg="red")
		b5.config(bg="red")
		b6.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
		b7.config(bg="red")
		b8.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
		b1.config(bg="red")
		b4.config(bg="red")
		b7.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
		b2.config(bg="red")
		b5.config(bg="red")
		b8.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
		b3.config(bg="red")
		b6.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
		b1.config(bg="red")
		b5.config(bg="red")
		b9.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
		b3.config(bg="red")
		b5.config(bg="red")
		b7.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	# Check if tie
	if count == 9 and winner == False:
		messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
		disable_all_buttons()


def b_click(b):
	global clicked, count

	if b["text"] == " " and clicked == True:
		b["text"] = "X"
		clicked = False
		count += 1
		checkifwon()
	elif b["text"] == " " and clicked == False:
		b["text"] = "O"
		clicked = True
		count += 1
		checkifwon()
	else:
		messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0


    b1 = Button(root, text = '',activeforeground = "Blue",background ='black',activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
    # b1.place(width =150,height = 150,y = 70,x = 0)

    b2 = Button(root, text = '',activeforeground = "Blue",background ='black',activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
    # b2.place(width =150,height = 150,y =220,x = 0)

    b3 = Button(root, text = "",activeforeground = "Blue",background ='black',activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
    # b3.place(width =150,height = 150,y = 370,x = 0)

    b4 = Button(root, text = "",activeforeground = "Blue",background ='black',activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
    # b4.place(width =150,height = 150,y = 70,x = 150)

    b5 = Button(root, text = "",activeforeground = "Blue",background ='black',activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
    # b5.place(width =150,height = 150,y = 220,x = 150 )

    b6 = Button(root, text = "",activeforeground = "Blue",background ='black',activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
    # b6.place(width =150,height = 150,y = 370,x = 150)

    b7 = Button(root, text = "",activeforeground = "Blue",background ='black',activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
    # b7.place(width =150,height = 150,y = 70,x = 300)

    b8 = Button(root, text = "",activeforeground = "Blue",background ='black',activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
    # b8.place(width =150,height = 150,y = 220,x = 300)

    b9 = Button(root, text = "",activeforeground = "Blue",background ='black',activebackground = "pink",pady=10,font=('Times New Roman', 25, 'bold'))
    # b9.place(width =150,height = 150,y = 370,x = 300)

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)

reset()




root.mainloop()

import os
import time
from tkinter import *

root = Tk()
root.geometry("600x400+40+80")
root.title('Mahjong')
current_directory = os.getcwd()


def bone_image(value):
    aw = current_directory + '/mahjong_tiles/' + value + '.gif'
    aww = PhotoImage(file=aw)
    return aww


bones = [
    [bone_image('d' + str(value + 1)) for value in range(9)],
    [bone_image('b' + str(value + 1)) for value in range(9)],
    [bone_image('c' + str(value + 1)) for value in range(9)],
    (
        [bone_image('W' + wind_type) for wind_type in ['e', 's', 'w', 'n']]
        + [bone_image('D' + dragon_type) for dragon_type in ['r', 'g', 'w']]
    )
]


def hand_bones():
    toplevel = Toplevel()
    #toplevel.geometry("600x400+40+80")
    toplevel.title('Another window')
    toplevel.focus_set()

    for y, bones_row in enumerate(bones):
        for x, bone in enumerate(bones_row):
            button = Button(toplevel, image=bone)
            button.grid(row=y+1, column=x+1)


def open_bones():
    print("123")


def closed_bones():
    print('143')


def winning_bone():
    print('win')


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
check1 = Checkbutton(root, text='Последняя со стены', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(root, text='Последняя из четырёх', variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(root, text='Ограбление конга', variable=var3, onvalue=1, offvalue=0)
check4 = Checkbutton(root, text='Замещающая для конга', variable=var4, onvalue=1, offvalue=0)
check1.grid(row=1, sticky=W, column=0)
check2.grid(row=1, column=1)
check3.grid(row=2, sticky=W, column=0)
check4.grid(row=2, column=1)

varRadio = IntVar()
varRadio.set(2)
rbutton1 = Radiobutton(root, text='Маджонг со стены', variable=varRadio, value=1)
rbutton2 = Radiobutton(root, text='Маджонг со снесённой кости', variable=varRadio, value=2)
rbutton1.grid(row=5, sticky=W, column=0)
rbutton2.grid(row=5, column=1)

label1 = Label(root, text='Свой ветер', fg='black', font='arial 14')
label1.grid(row=7, sticky=W, column=0)
variable = StringVar(root)
variable.set("Восточный") # default value

w1 = OptionMenu(root, variable, "Восточный", "Южный", "Западный", "Северный")
w1.grid(row=7, column=1)
label2 = Label(root, text='Ветер раунда', fg='black', font='arial 14')
label2.grid(row=8, sticky=W, column=0)
variable = StringVar(root)
variable.set("Восточный") # default value
w2 = OptionMenu(root, variable, "Восточный", "Южный", "Западный", "Северный")
w2.grid(row=8, column=1)

label3 = Label(root, text='Количество цветов', fg='black', font='arial 14')
label3.grid(row=9, sticky=W, column=0)
variable = StringVar(root)
variable.set("0") # default value
w3 = OptionMenu(root, variable, '0', '1', '2', '3', '4', '5', '6', '7', '8')
w3.grid(row=9, column=1)

button1 = Button(root, text='Кости в открытую', command=open_bones)
button2 = Button(root, text='Кости в руке', command=hand_bones)
button3 = Button(root, text='Кости в закрытую', command=closed_bones)
button4 = Button(root, text='Победная кость', command=winning_bone)
button5 = Button(root, text='что-тоянепомнюдлячегоона')
button1.grid(row=10, sticky=W, column=0, columnspan=3)
button2.grid(row=11, sticky=W, column=0)
button3.grid(row=12, sticky=W, column=0)
button4.grid(row=13, sticky=W, column=0)
button5.grid(row=14, sticky=W, column=0)

# button1 = Button(root, text='ok', fg='black', font='arial 14', command=hand_bones)
# button1.grid(row=3, column=3)







root.mainloop()

import os
import time
from tkinter import *

root = Tk()
root.geometry("600x600+40+80")
root.title('Mahjong')
current_directory = os.getcwd()

concealed = []
melded = []
winning = []
hand = []


def bone_image(value):
    aw = current_directory + '/mahjong_tiles/' + value + '.gif'
    aww = PhotoImage(file=aw)
    return aww


bones = [
    ['d' + str(value + 1) for value in range(9)],
    ['b' + str(value + 1) for value in range(9)],
    ['c' + str(value + 1) for value in range(9)],
    (
        ['W' + wind_type for wind_type in ['e', 's', 'w', 'n']]
        + ['D' + dragon_type for dragon_type in ['r', 'g', 'w']]
    )
]

bone_images = [[bone_image(value) for value in row] for row in bones]


def on_bone_click(type, x, y):
    bone = bones[y][x]
    img = bone_images[y][x]
    print(x, y, bone)

    if type == 'h':
        image_container = Label(hand_grid, image=img)
        image_container.grid(row=11, sticky=W, column=len(hand))

        bone_object = {'bone': bone, 'image': image_container, 'row': 11}
        hand.append(bone_object)

        image_container.bind('<Button-1>', lambda e: remove_image(bone_object, hand))

    if type == 'm':
        image_container = Label(open_grid, image=img)
        image_container.grid(row=10, sticky=W, column=len(melded))
        melded.append({'bone': bone, 'image': image_container})

    if type == 'c':
        image_container = Label(close_grid, image=img)
        image_container.grid(row=10, sticky=W, column=len(concealed))
        concealed.append({'bone': bone, 'image': image_container})

    if type == 'w':
        image_container = Label(winning_grid, image=img)
        image_container.grid(row=10, sticky=W, column=len(winning))
        winning.append({'bone': bone, 'image': image_container})


def render_images():
    pass


def remove_image(bone_object, array):
    index = array.index(bone_object)
    bone_image = array[index]['image']
    bone_image.destroy()
    array.remove(bone_object)

    for index, bone_object in enumerate(array):
        bone_object['image'].grid(row=bone_object['row'], sticky=W, column=index)


def bones_list(title, type):
    toplevel = Toplevel()
    toplevel.title(title)
    toplevel.focus_set()
    for y, bones_row in enumerate(bone_images):
        for x, bone in enumerate(bones_row):
            button = Button(toplevel, image=bone, command=lambda x=x, y=y: on_bone_click(type, x, y))
            button.grid(row=y+1, column=x+1)


def calculate():
    print('new')
    print(melded)
    print(hand)
    print(concealed)
    print(winning)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
check1 = Checkbutton(root, text='Последняя со стены', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(root, text='Последняя из четырёх', variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(root, text='Ограбление конга', variable=var3, onvalue=1, offvalue=0)
check4 = Checkbutton(root, text='Замещающая для конга', variable=var4, onvalue=1, offvalue=0)
check1.grid(row=1, sticky=W, column=0)
check2.grid(row=1, sticky=W, column=1)
check3.grid(row=2, sticky=W, column=0)
check4.grid(row=2, sticky=W, column=1)

varRadio = IntVar()
varRadio.set(2)
rbutton1 = Radiobutton(root, text='Маджонг со стены', variable=varRadio, value=1)
rbutton2 = Radiobutton(root, text='Маджонг со снесённой кости', variable=varRadio, value=2)
rbutton1.grid(row=3, sticky=W, column=0)
rbutton2.grid(row=3, sticky=W, column=1)

label1 = Label(root, text='Свой ветер', fg='black', font='arial 14')
label1.grid(row=4, sticky=W, column=0)
variable = StringVar(root)
variable.set("Восточный") # default value

w1 = OptionMenu(root, variable, "Восточный", "Южный", "Западный", "Северный")
w1.grid(row=4, sticky=W, column=1)
label2 = Label(root, text='Ветер раунда', fg='black', font='arial 14')
label2.grid(row=5, sticky=W, column=0)
variable = StringVar(root)
variable.set("Восточный") # default value
w2 = OptionMenu(root, variable, "Восточный", "Южный", "Западный", "Северный")
w2.grid(row=5, sticky=W, column=1)

label3 = Label(root, text='Количество цветов', fg='black', font='arial 14')
label3.grid(row=6, sticky=W, column=0)
variable = StringVar(root)
variable.set("0") # default value
w3 = OptionMenu(root, variable, '0', '1', '2', '3', '4', '5', '6', '7', '8')
w3.grid(row=6, sticky=W, column=1)

button1 = Button(
    root, text='Кости в открытую', command=lambda title='Кости в открытую', type='m': bones_list(title, type))
button2 = Button(
    root, text='Кости в руке', command=lambda title='Кости в руке', type='h': bones_list(title, type))
button3 = Button(
    root, text='Кости в закрытую', command=lambda title='Кости в закрытую', type='c': bones_list(title, type))
button4 = Button(
    root, text='Победная кость', command=lambda title='Победная кость', type='w': bones_list(title, type))
button5 = Button(
    root, text='что-тоянепомнюдлячегоона', command=calculate)
button1.grid(row=10, sticky=W, column=0)
button2.grid(row=11, sticky=W, column=0)
button3.grid(row=12, sticky=W, column=0)
button4.grid(row=13, sticky=W, column=0)
button5.grid(row=14, sticky=W, column=0)

open_grid = Frame(root)
open_grid.grid(row=10, sticky=W, column=1)
hand_grid = Frame(root)
hand_grid.grid(row=11, sticky=W, column=1)
close_grid = Frame(root)
close_grid.grid(row=12, sticky=W, column=1)
winning_grid = Frame(root)
winning_grid.grid(row=13, sticky=W, column=1)

# button1 = Button(root, text='ok', fg='black', font='arial 14', command=hand_bones)
# button1.grid(row=3, column=3)







root.mainloop()

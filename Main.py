import os
import time
from tkinter import *
root=Tk()
root.geometry("600x400+40+80")
root.title('Mahjong')
current_directory = os.getcwd()


def bone(value):
    aw = current_directory + '\mahjong_tiles/' + value + '.png'
    aww = PhotoImage(file=aw)
    return aww


dot1 = bone('d1')
dot2 = bone('d2')
dot3 = bone('d3')
dot4 = bone('d4')
dot5 = bone('d5')
dot6 = bone('d6')
dot7 = bone('d7')
dot8 = bone('d8')
dot9 = bone('d9')
bam1 = bone('b1')
bam2 = bone('b2')
bam3 = bone('b3')
bam4 = bone('b4')
bam5 = bone('b5')
bam6 = bone('b6')
bam7 = bone('b7')
bam8 = bone('b8')
bam9 = bone('b9')
tra1 = bone('c1')
tra2 = bone('c2')
tra3 = bone('c3')
tra4 = bone('c4')
tra5 = bone('c5')
tra6 = bone('c6')
tra7 = bone('c7')
tra8 = bone('c8')
tra9 = bone('c9')
dr = bone('Dr')
dg = bone('Dg')
dw = bone('Dw')
we = bone('We')
ws = bone('Ws')
ww = bone('Ww')
wn = bone('Wn')


def hand_bones():
    toplevel = Toplevel()
    #toplevel.geometry("600x400+40+80")
    toplevel.title('Another window')
    toplevel.focus_set()

    button_d1 = Button(toplevel, image=dot1)
    button_d1.grid(row=1, column=1)
    button_d2 = Button(toplevel, image=dot2)
    button_d2.grid(row=1, column=2)
    button_d3 = Button(toplevel, image=dot3)
    button_d3.grid(row=1, column=3)
    button_d4 = Button(toplevel, image=dot4)
    button_d4.grid(row=1, column=4)
    button_d5 = Button(toplevel, image=dot5)
    button_d5.grid(row=1, column=5)
    button_d6 = Button(toplevel, image=dot6)
    button_d6.grid(row=1, column=6)
    button_d7 = Button(toplevel, image=dot7)
    button_d7.grid(row=1, column=7)
    button_d8 = Button(toplevel, image=dot8)
    button_d8.grid(row=1, column=8)
    button_d9 = Button(toplevel, image=dot9)
    button_d9.grid(row=1, column=9)

    button_b1 = Button(toplevel, image=bam1)
    button_b1.grid(row=2, column=1)
    button_b2 = Button(toplevel, image=bam2)
    button_b2.grid(row=2, column=2)
    button_b3 = Button(toplevel, image=bam3)
    button_b3.grid(row=2, column=3)
    button_b4 = Button(toplevel, image=bam4)
    button_b4.grid(row=2, column=4)
    button_b5 = Button(toplevel, image=bam5)
    button_b5.grid(row=2, column=5)
    button_b6 = Button(toplevel, image=bam6)
    button_b6.grid(row=2, column=6)
    button_b7 = Button(toplevel, image=bam7)
    button_b7.grid(row=2, column=7)
    button_b8 = Button(toplevel, image=bam8)
    button_b8.grid(row=2, column=8)
    button_b9 = Button(toplevel, image=bam9)
    button_b9.grid(row=2, column=9)

    button_c1 = Button(toplevel, image=tra1)
    button_c1.grid(row=3, column=1)
    button_c2 = Button(toplevel, image=tra2)
    button_c2.grid(row=3, column=2)
    button_c3 = Button(toplevel, image=tra3)
    button_c3.grid(row=3, column=3)
    button_c4 = Button(toplevel, image=tra4)
    button_c4.grid(row=3, column=4)
    button_c5 = Button(toplevel, image=tra5)
    button_c5.grid(row=3, column=5)
    button_c6 = Button(toplevel, image=tra6)
    button_c6.grid(row=3, column=6)
    button_c7 = Button(toplevel, image=tra7)
    button_c7.grid(row=3, column=7)
    button_c8 = Button(toplevel, image=tra8)
    button_c8.grid(row=3, column=8)
    button_c9 = Button(toplevel, image=tra9)
    button_c9.grid(row=3, column=9)

    button_we = Button(toplevel, image=we)
    button_we.grid(row=4, column=1)
    button_ws = Button(toplevel, image=ws)
    button_ws.grid(row=4, column=2)
    button_ww = Button(toplevel, image=ww)
    button_ww.grid(row=4, column=3)
    button_wn = Button(toplevel, image=wn)
    button_wn.grid(row=4, column=4)
    button_dr = Button(toplevel, image=dr)
    button_dr.grid(row=4, column=5)
    button_dg = Button(toplevel, image=dg)
    button_dg.grid(row=4, column=6)
    button_dw = Button(toplevel, image=dw)
    button_dw.grid(row=4, column=7)


def open_bones():
    print("123")


def closed_bones():
    print('143')


def winning_bone():
    print('win')


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
check1=Checkbutton(root,text='Последняя со стены',variable=var1,onvalue=1,offvalue=0)
check2=Checkbutton(root,text='Последняя из четырёх',variable=var2,onvalue=1,offvalue=0)
check3=Checkbutton(root,text='Ограбление конга',variable=var3,onvalue=1,offvalue=0)
check4=Checkbutton(root,text='Замещающая для конга',variable=var4,onvalue=1,offvalue=0)
check1.grid(row=1,sticky=W,column=0)
check2.grid(row=1,column=1)
check3.grid(row=2,sticky=W,column=0)
check4.grid(row=2,column=1)

varRadio=IntVar()
rbutton1=Radiobutton(root,text='Маджонг со стены',variable=varRadio,value=1)
rbutton2=Radiobutton(root,text='Маджонг со снесённой кости',variable=varRadio,value=2)
rbutton1.grid(row=5,sticky=W,column=0)
rbutton2.grid(row=5,column=1)
label1=Label(root,text='Свой ветер',fg='black',font='arial 14')
label1.grid(row=7,sticky=W,column=0)
variable = StringVar(root)
variable.set("Восточный") # default value
w1 = OptionMenu(root, variable, "Восточный", "Южный", "Западный", "Северный")
w1.grid(row=7,column=1)
label2=Label(root,text='Ветер раунда',fg='black',font='arial 14')
label2.grid(row=8,sticky=W,column=0)
variable = StringVar(root)
variable.set("Восточный") # default value
w2 = OptionMenu(root, variable, "Восточный", "Южный", "Западный", "Северный")
w2.grid(row=8,column=1)
label3=Label(root,text='Количество цветов',fg='black',font='arial 14')
label3.grid(row=9,sticky=W,column=0)
variable = StringVar(root)
variable.set("0") # default value
w3 = OptionMenu(root, variable, '0', '1', '2', '3', '4', '5', '6', '7', '8')
w3.grid(row=9,column=1)

button1=Button(root, text='Кости в открытую', command=open_bones)
button2=Button(root, text='Кости в руке', command=hand_bones)
button3=Button(root, text='Кости в закрытую',command=closed_bones)
button4=Button(root, text='Победная кость',command=winning_bone)
button5=Button(root, text='что-тоянепомнюдлячегоона')
button1.grid(row=10,sticky=W,column=0,columnspan=3)
button2.grid(row=11,sticky=W,column=0)
button3.grid(row=12,sticky=W,column=0)
button4.grid(row=13,sticky=W,column=0)
button5.grid(row=14,sticky=W,column=0)

# button1 = Button(root, text='ok', fg='black', font='arial 14', command=hand_bones)
# button1.grid(row=3, column=3)







root.mainloop()

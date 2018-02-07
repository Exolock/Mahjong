import os
import time
from tkinter import *
root = Tk()
root.geometry("600x400+1080+80")
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


def hand_bones():
    toplevel = Toplevel()
    toplevel.geometry("600x400+40+80")
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

button1 = Button(root, text='ok', fg='black', font='arial 14', command=hand_bones)
button1.grid(row=3, column=3)







root.mainloop()

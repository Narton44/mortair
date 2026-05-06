from tkinter import *
import math

root = Tk()

root.title('АРТА')
root.geometry('777x777')
root.resizable(1, 1)
root['bg'] = 'green'



# ----------------------Прямая геодезическая задача----------------------

label_x = Label(
    root,
    text='Х позиции',
    width=11,
    )
label_x.place(x=0,y=0)

label_y = Label(
    root,
    text='Y позиции',
    width=11,
    )
label_y.place(x=0,y=50)

label_d = Label(
    root,
    text='Дистанция',
    width=11,
    )
label_d.place(x=0,y=90)

label_angle = Label(
    root,
    text='Дирекц. угол',
    width=11,
    )
label_angle.place(x=0,y=135)

label_aim_coords = Label(
    root,
    text=' ',
    width=27,
    height=2,
    )
label_aim_coords.place(x=0,y=250)


position_x = Entry(
    root,
)
# position_x.insert(0, "Х позиции")
position_x.place(x=0,y=20)

position_y = Entry(
    root,
)
# position_y.insert(0, "Y позиции")
position_y.place(x=0,y=65)

distance = Entry(
    root,
)
# distance.insert(0, "Дистанция")
distance.place(x=0,y=110)

dir_angle = Entry(
    root,
)
# angle.insert(0, "Дистанция")
dir_angle.place(x=0,y=155)


def find_aim_x_y(): # сам метод расчета коодинат цели

    pos_x=float(position_x.get())
    pos_y=float(position_y.get())
    dist=float(distance.get())
    dir_ang=math.radians(float(dir_angle.get()))
    # dir_ang_rad = math.radians(dir_ang)  # Обязательно!

    aim_x = round(pos_x + dist * math.cos(dir_ang),3)
    aim_y = round(pos_y + dist * math.sin(dir_ang),3)
    label_aim_coords.configure(text=f'X цели={aim_x}, Y цели={aim_y}')


btn = Button( # кнопка запуска расчета коодинат цели
    root,
    text='Рассчитать координаты цели',
    command=find_aim_x_y,
    font=('Comic Sans MS', 10, 'bold'),
    cursor='hand2',
    )
btn.place(x=0,y=180)



mainloop()

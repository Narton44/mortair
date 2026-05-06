from tkinter import *
import math

root = Tk()

root.title('АРТА')
root.geometry('777x400')
root.resizable(1, 1)
root['bg'] = 'green'
# root.iconbitmap('mortar_81.ico')



# ----------------------Прямая геодезическая задача----------------------

label_x = Label(
    root,
    text='Х позиции',
    width=11,
    )
label_x.place(x=10,y=50)

position_x = Entry(
    root,
)
# position_x.insert(0, "Х позиции")
position_x.place(x=10,y=70)

label_y = Label(
    root,
    text='Y позиции',
    width=11,
    )
label_y.place(x=10,y=97)

position_y = Entry(
    root,
)
# position_y.insert(0, "Y позиции")
position_y.place(x=10,y=115)

label_d = Label(
    root,
    text='Дистанция',
    width=11,
    )
label_d.place(x=10,y=140)

distance = Entry(
    root,
)
# distance.insert(0, "Дистанция")
distance.place(x=10,y=160)

label_angle = Label(
    root,
    text='Дирекц. угол',
    width=11,
    )
label_angle.place(x=10,y=185)

dir_angle = Entry(
    root,
)
# dir_angle.insert(0, "Дирекционный угол")
dir_angle.place(x=10,y=205)

label_aim_coords = Label(
    root,
    text=' ',
    font=(None, 10, "bold"),
    width=24,
    height=2,
    )
label_aim_coords.place(x=10,y=300)


def find_aim_x_y(): # сам метод расчета коодинат цели

    pos_x=float(position_x.get())
    pos_y=float(position_y.get())
    dist=float(distance.get())
    dir_ang=math.radians(float(dir_angle.get()))

    aim_x = round(pos_x + dist * math.cos(dir_ang),4)
    aim_y = round(pos_y + dist * math.sin(dir_ang),4)
    label_aim_coords.configure(text=f'X цели={aim_x}\nY цели={aim_y}')


btn = Button( # кнопка запуска расчета коодинат цели
    root,
    text='Рассчитать координаты цели',
    command=find_aim_x_y,
    font=('Comic Sans MS', 10, 'bold'),
    cursor='hand2',
    )
btn.place(x=10,y=230)


# ----------------------Обратная геодезическая задача----------------------

ogz_frame = Frame(root)
ogz_frame.pack(padx=250,pady=50)

fire_point_x = Label(ogz_frame, text="X позиции")  # Сохраняем ссылку
fire_point_x.grid(row=0, column=0)  # Размещаем отдельно




mainloop()

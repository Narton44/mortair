from tkinter import *
import math

root = Tk()

root.title('АРТА')
root.geometry('800x400')
root.resizable(0, 0)
root['bg'] = 'green'
root.iconbitmap('mortar_81.ico')


# ----------------------------- Фрэймы ---------------------------------
pgz_frame = Frame(root, width=400 ,height=350, bg='dark green')
ogz_frame = Frame(root, width=400 ,height=350, bg='green')
result_frame = Frame(root, width=800, height=50, bg='black')



pgz_frame.grid(row=0, column=0)
ogz_frame.grid(row=0, column=1)
result_frame.grid(row=1, column=0, columnspan=2)

# ----------------------Прямая геодезическая задача----------------------

label_title_pgz = Label(pgz_frame, text='Прямая геодезическая задача', font=(None, 10, "bold"), width=46, height=1)
label_title_pgz.place(x=10,y=6)

label_x = Label(pgz_frame, text='Х позиции', width=11,)
label_x.place(x=10,y=50)

position_x = Entry(pgz_frame)
position_x.insert(0,'0')
position_x.place(x=10,y=70)


label_y = Label(pgz_frame, text='Y позиции', width=11,)
label_y.place(x=10,y=97)

position_y = Entry(pgz_frame)
position_y.insert(0,'0')
position_y.place(x=10,y=115)


label_d = Label(pgz_frame, text='Дистанция', width=11,)
label_d.place(x=10,y=140)

distance = Entry(pgz_frame)
distance.insert(0,'2150')
distance.place(x=10,y=160)


label_angle = Label(pgz_frame, text='Дирекц. угол', width=11)
label_angle.place(x=10,y=185)

dir_angle = Entry(pgz_frame)
dir_angle.insert(0,'1532')
dir_angle.place(x=10,y=205)


label_aim_coords = Label(result_frame, text=' ', font=(None, 10, "bold"), width=46, height=2)
label_aim_coords.place(x=10,y=6)


def find_aim_x_y(): # сам метод расчета коодинат цели

    pos_x=float(position_x.get())
    pos_y=float(position_y.get())
    dist=float(distance.get())
    int_distance = math.radians(float(str(dir_angle.get())[:2])*6)
    fract_distance = math.radians(float(str(dir_angle.get())[2:])*0.06)
    dir_ang = int_distance + fract_distance

    aim_x = round(pos_x + dist * math.cos(dir_ang),4)
    aim_y = round(pos_y + dist * math.sin(dir_ang),4)
    label_aim_coords.configure(text=f'X цели={aim_x}\nY цели={aim_y}')


btn = Button( # кнопка запуска расчета коодинат цели
    pgz_frame,
    text='Рассчитать координаты цели',
    command=find_aim_x_y,
    font=('Comic Sans MS', 10, 'bold'),
    cursor='hand2',
    )
btn.place(x=10,y=230)


# # ----------------------Обратная геодезическая задача----------------------

label_title_ogz = Label(ogz_frame, text='Обратная геодезическая задача', font=(None, 10, "bold"), width=46, height=1)
label_title_ogz.place(x=10,y=6)

label_firepoint_x = Label(ogz_frame, text='Х позиции', width=11,)
label_firepoint_x.place(x=10,y=50)

entry_firepoint_x = Entry(ogz_frame)
entry_firepoint_x.insert(0,'0')
entry_firepoint_x.place(x=10,y=70)


label_firepoint_y = Label(ogz_frame, text='Y позиции', width=11)
label_firepoint_y.place(x=10,y=97)

entry_firepoint_y = Entry(ogz_frame)
entry_firepoint_y.insert(0,'0')
entry_firepoint_y.place(x=10,y=115)


label_aim_x = Label(ogz_frame, text='Х цели', width=11,)
label_aim_x.place(x=10,y=140)

entry_aim_x = Entry(ogz_frame)
entry_aim_x.insert(0,'400')
entry_aim_x.place(x=10,y=160)


label_aim_y = Label(ogz_frame, text='Y цели', width=11,)
label_aim_y.place(x=10,y=185)

entry_aim_y = Entry(ogz_frame)
entry_aim_y.insert(0,'400')
entry_aim_y.place(x=10,y=205)


label_angle_and_distance = Label(result_frame, text=' ', font=(None, 10, "bold"), width=46, height=2)
label_angle_and_distance.place(x=410,y=6)


def find_angle_and_distance(): # сам метод расчета дирекционного угла и дистанции до цели

    delta_x=float(entry_aim_x.get()) - float(entry_firepoint_x.get())
    delta_y=float(entry_aim_y.get()) - float(entry_firepoint_y.get())
    
    dist = round(math.sqrt(delta_x**2 + delta_y**2),2)

    rhumb = math.atan(delta_y / delta_x)

    if delta_x > 0 and delta_y > 0:
        dir_ang = math.radians(rhumb)*180/math.pi
    elif delta_x < 0 and delta_y > 0:
        dir_ang = math.radians(180 - rhumb)*180/math.pi
    elif delta_x < 0 and delta_y < 0:
        dir_ang = math.radians(180 + rhumb)*180/math.pi
    elif delta_x > 0 and delta_y < 0:
        dir_ang = math.radians(360 - rhumb)*180/math.pi


    label_angle_and_distance.configure(text=f'Дирекционный угол: {dir_ang}\nДистанция: {dist}')
    print(rhumb)
btn = Button( # кнопка запуска расчета дирекционного угла и дистанции до цели
    ogz_frame,
    text='Рассчитать дирекционный угол и дистанцию',
    command=find_angle_and_distance,
    font=('Comic Sans MS', 10, 'bold'),
    cursor='hand2',
    )
btn.place(x=10,y=230)


mainloop()
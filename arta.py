from tkinter import *

root = Tk()

root.iconbitmap('mortar_81.ico')
root.title('АРТА')
root.geometry('777x777')
root.resizable(1, 1)
# root.config(bg='black')
root['bg'] = 'green'

label = Label(
    root,
    text='Огонь из 120!',
    font=('Comic Sans MS', 20, 'bold'),
    bg='brown',
    width=11,
    )

label.pack()
label.place(x=0,y=0, anchor='nw')

def big_click():
    print('БАДА БУМ!!!')

btn = Button(
    root,
    text='Огонь из 120!',
    command=big_click,
    font=('Comic Sans MS', 20, 'bold'),
    bg='lime',
    activebackground='red',
    activeforeground='blue',
    width=11,
    cursor='hand2',
    )

btn.pack()
btn.place(x=0,y=43)


position_x = Entry(
    root,
    text='Х позиции'
)
position_x.place(x=100,y=200)


mainloop()

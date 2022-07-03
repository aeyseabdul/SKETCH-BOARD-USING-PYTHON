from tkinter import *
from tkinter import ttk

current_x = 0
current_y = 0
color = 'black'
def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y
    board.create_line((current_x, current_y, work.x, work.y), width=get_currentsize(), fill=color,capstyle=ROUND,smooth=TRUE)
    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color
    color = new_color

def size(event):
    value.configure(text=get_currentsize())

def get_currentsize():
    return '{:.0f}'.format(currentsize.get())

def new_canvas():
    board.delete('all')
    display_pallete()

root = Tk()
root.geometry("1050x570")
root.resizable(False, False)
root.title("Sketch Art")
icon=PhotoImage(file="pencil-icon.png")
root.iconphoto(False,icon)

board=Canvas(root,bg="#ffffff",width=1025,height=450, cursor="hand2")
board.place(relx=0.5,rely=0.5,y=50,anchor=CENTER)
tools=Canvas(root,bg="#ffffff",width=370, height=60).place(x=350,y=20)
colors=Canvas(root,bg="#ffffff",width=310, height=40)
colors.place(x=360,y=30)

eraser=PhotoImage(file="eraser-icon1.png")
Button(root,image=eraser,relief="flat",bg="#ffffff",command=new_canvas).place(x=680,y=35)

currentsize=DoubleVar()
brushsize=ttk.Scale(root,from_=0,to=100,length=200,command=size,variable=currentsize,orient=HORIZONTAL)
brushsize.place(x=750,y=45)
value=Label(root,font=('Poppins',15),text=get_currentsize())
value.place(x=960,y=35)
text=Label(root,text="Brush Size:")
text.place(x=750,y=25)

def display_pallete():
    id = colors.create_rectangle((10, 10, 30, 30), fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10+30, 10, 30+30, 30), fill="yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((10+30+30, 10, 30+30+30, 30), fill="green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10+30+30+30, 10, 30+30+30+30, 30), fill="blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10+30+30+30+30, 10, 30+30+30+30+30, 30), fill="pink")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('pink'))

    id = colors.create_rectangle((10+30+30+30+30+30, 10, 30+30+30+30+30+30, 30), fill="purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

    id = colors.create_rectangle((10+30+30+30+30+30+30, 10, 30+30+30+30+30+30+30, 30), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10+30+30+30+30+30+30+30, 10, 30+30+30+30+30+30+30+30, 30), fill="orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10+30+30+30+30+30+30+30+30+30, 10, 30+30+30+30+30+30+30+30+30+30, 30), fill='white')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('white'))

display_pallete()

board.bind('<Button-1>', locate_xy)
board.bind('<B1-Motion>', addLine)

root.mainloop()

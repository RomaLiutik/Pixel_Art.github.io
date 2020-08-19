from tkinter import*
from tkinter.filedialog import asksaveasfile, askopenfile
from PIL import Image, ImageDraw

tk = Tk()
tk.title('Pixel Art')
tk.geometry('500x320')
tk.resizable(0,0)
tk['bg'] = 'gray'

color = 'black'
cns = ''

white = (255,255,255)
Frame_Color = Frame(tk, borderwidth = 3, relief=RAISED)

scr = Scrollbar(tk, orient=VERTICAL)
#scr.pack(side='right', fill='y')

Frame_Color.configure(Frame_Color.place(x = 372, y = 5))
Frame_Color.place(x = 372, y = 5)

menu = Menu(tk)
tk.configure(menu=menu)

File = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=File)
File.add_command(label='Clear', command = lambda : clear())
File.add_command(label='Save as', command = lambda : save_as())

Frame_Work_Space = Frame(tk, borderwidth = 3, relief=RAISED)
Frame_Work_Space['bg'] = 'black'
Frame_Work_Space.place(x = 50, y = 5)

Frame_line_color_one = Frame(Frame_Color)
Frame_line_color_one.pack()

Frame_line_color_two = Frame(Frame_Color)
Frame_line_color_two.pack(side = BOTTOM)

bttn_black = Button(Frame_line_color_one, height = 1, width = 2, command = lambda : change_color('#000000'))
bttn_black['bg'] = '#000000'
bttn_black.pack( side = LEFT )

bttn_white = Button(Frame_line_color_one, height = 1, width = 2, command = lambda : change_color('#ffffff'))
bttn_white['bg'] = '#ffffff'
bttn_white.pack( side = LEFT )

bttn_none_1_1 = Button(Frame_line_color_one, height = 1, width = 2)
bttn_none_1_1.pack( side = LEFT )

bttn_none_2_1 = Button(Frame_line_color_one, height = 1, width = 2)
bttn_none_2_1.pack( side = LEFT )

bttn_none_3_1 = Button(Frame_line_color_one, height = 1, width = 2)
bttn_none_3_1.pack( side = LEFT )

bttn_red = Button(Frame_line_color_two, height = 1, width = 2, command = lambda : change_color('#ff0000'))
bttn_red['bg'] = '#ff0000'
bttn_red.pack( side = LEFT )

bttn_green = Button(Frame_line_color_two, height = 1, width = 2, command = lambda : change_color('#00ff00'))
bttn_green['bg'] = '#00ff00'
bttn_green.pack( side = LEFT )

bttn_blue = Button(Frame_line_color_two, height = 1, width = 2, command = lambda : change_color('#0000ff'))
bttn_blue['bg'] = '#0000ff'
bttn_blue.pack( side = LEFT )

bttn_none_1_2 = Button(Frame_line_color_two, height = 1, width = 2)
bttn_none_1_2.pack( side = LEFT )

bttn_none_2_2 = Button(Frame_line_color_two, height = 1, width = 2)
bttn_none_2_2.pack( side = LEFT )

image1 = Image.new('RGB', (300,300), white)
draw = ImageDraw.Draw(image1)

def save_as():
    
    file = asksaveasfile(mode='w', defaultextension = 'jpg')
    image1.save(file)
def change_color(new_color):
    global color
    color = new_color

def create_work_cpace():
    global cns
    cns = Canvas(Frame_Work_Space, width = 300, height = 300)
    cns['bg'] = '#ffffff'
    cns.pack()

def create_lines():
    a = 0
    while a != 15:
        cns.create_line(20*a,0,20*a,320, tag='line')
        a = a + 1
    a = 0
    while a != 15:
        cns.create_line(0,20*a, 320, 20*a, tag = 'line')
        a = a +1

def clear():
    global cns, draw, image1
    cns.delete('all')
    create_lines()
    del draw, image1
    image1 = Image.new('RGB', (300,300), white)

    draw = ImageDraw.Draw(image1)



def coords_coorsor(event):
    global color
    x = event.x
    y = event.y
    s = 0
    while s != 15:
        f = s*20
        if x > f:
            if x < f+20:
                x_ = s
        if y > f:
            if y < f+20:
                y_ = s
        s = s + 1
    
    try:
        x1 = x_*20
        y1 = y_*20
        cns.create_rectangle(x1,y1,x1 + 20,y1 + 20, fill=color, outline=color)
        draw.rectangle([(x1,y1),(x1+20,y1+20)], fill=color, outline=color)
    except:
        pass
    create_lines()



create_work_cpace()
create_lines()
cns.bind('<Button-1>', coords_coorsor)
tk.mainloop()

# -*- coding: utf-8 -*-
import random
from PIL import Image,ImageDraw,ImageFilter,Image, ImageTk
import re
import tkinter as tk
import time

scr_x = 800  # Ширина картинки
scr_y = scr_x  # Высота картинки
img = Image.new('RGB', (scr_x, scr_y), 'black')  # Создадим картинку с черным цветом фона
canvas = img.load()  # Через эту переменную у нас есть доступ к пикселям картинки or pixel_access_object
idraw = ImageDraw.Draw(img)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self, color=None):
        canvas[self.x, scr_y - self.y] = color or (255, 255, 255)

    def copy(self):
        return Point(self.x, self.y)


def zero_div(a, b):
    return float(a) / b if b else 0


def triangle(coords, color):
    a, b, c = sorted(coords, key=lambda p: p.y)
    p1 = a.copy()  # <__main__.Point object at 0x00000265FD9B6430>

    p2 = a.copy()

    delta_p1 = zero_div((b.x - a.x), (b.y - a.y))
    # print("delta_p1",delta_p1)
    delta_p2 = zero_div((c.x - a.x), (c.y - a.y))
    # print("delta_p2", delta_p2)
    for y in (b.y, c.y):
        while p1.y < y:
            if p1.x > p2.x:
                p3 = p2.copy()
                x = p1.x
            else:
                p3 = p1.copy()
                x = p2.x
            while p3.x < x:
                p3.show(color)
                p3.x += 1
            # print("1 p1y-",p1.y,"p2y-",p2.y)
            p1.y += 1
            p2.y += 1  # идет отрисовка сверху вниз

            # print("2 p1y-", p1.y, "p2y-", p2.y)
            # print("p1",p1.x,"p2",p2.x)
            p1.x += delta_p1
            p2.x += delta_p2
        delta_p1 = zero_div((c.x - b.x), (c.y - b.y))


def paint(o, p):
    half_scr_x = int(scr_x / 2)
    half_scr_y = int(scr_y / 2)
    f = open('face.obj', 'r')
    lines = f.read()  # читаем файл циликом
    # print(lines)
    points = []

    for line in lines.split('\n'):
        try:
            v, x, y, z = re.split('\s+', line)
            # print("v",v,"x",x,"y",y,"z",z)
        except:
            continue
        if v == 'v':
            print("v",v,"x",x,"y",y,"z",z)
            # короч смотри у нас есть масив "векторов" points и мы читаем по x ,y ,z координаты и вектора по ним в оригинале
            # был только x and z
            x = int((float(x) + 1) * half_scr_x)
            y = int((float(y) + 1) * half_scr_y)
            z = int((float(z) + 1) * half_scr_x)
            if y == 300:
                print(y)
            question = x * o + z * p
            # points.append(Point(z, y))
            points.append(Point(question, y))
        if v == 'f':
            # print("v", v, "x", x, "y", y, "z", z)
            # color = tuple([random.randint(0, 255)] * 3)
            color = tuple([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
            triangle([points[int(i.split('/')[0]) - 1] for i in (x, y, z)], color)
            # print([points[int(i.split('/')[0])-1] for i in (x, y, z)])#короче выбираются треугольники из 3 векторов и их расскрашивают


def rotate():
    o = 0.7
    p = 0.7
    paint(o, p)
    print('ready')


#-------------------------------------------------------------------------
def on_click(event=None):
    # `command=` calls function without argument
    # `bind` calls function with one argument
    indextest = 0
    print("image clicked")
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    x1 = root.winfo_rootx()
    y1 = root.winfo_rooty()
    abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
    abs_coord_y = root.winfo_pointery() - root.winfo_rooty()
    print("root.winfo_root", x1 ,y1)
    print("abs_coord",abs_coord_x, abs_coord_y)
    print("root.winfo_pointer",x,y)
    print("______________________________________")
    idraw.rectangle((0,0,800,800),fill="black")
    rotate()
    photo1 = ImageTk.PhotoImage(img)
    l.configure(image=photo1)
    l.image = photo1
# --- main ---


#------------------------------------------------------------------
paint(1, 0)
print(img.format)
print(img.size)
print(img.mode)
# img.onkey(rotate,"r")
# img.listen()
#================================
# init
root = tk.Tk()
index = 0
# load image
photo = ImageTk.PhotoImage(img)

# label with image
l = tk.Label(root, image=photo)
l.pack()

# bind click event to image
l.bind('<Button-1>', on_click)


# button with image binded to the same function
#b = tk.Button(root, image=photo, command=on_click)
#b.pack()

# button with text closing window
b = tk.Button(root, text="Close", command=root.destroy)
b.pack()

# "start the engine"
root.mainloop()

#====================================
#img.show()
#=========================================

# time.sleep(1)
# idraw.rectangle((0,0,800,800),fill="black")
# rotate()
# img.show()


# короче не ищи а расчитывай x and z (sinx and cosx) a y будет найден по клику мышки
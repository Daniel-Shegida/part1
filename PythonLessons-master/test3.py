import tkinter as tk
from PIL import Image, ImageTk

# --- functions ---

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
    print(index)
    print('test',indextest)
    #if index == 0 :
    #    l.configure(image=photo1)
    #    l.image = photo1
    #    indextest += 1
    #else :
    #    l.configure(image=photo)
    #    l.image = photo
    l.configure(image=photo1)


def plus (index):
    print('index',index)
    index +=1
# --- main ---

# init
root = tk.Tk()
index = 0
# load image
image = Image.open("image.png")
photo = ImageTk.PhotoImage(image)
image1 = Image.open("image2.png")
photo1 = ImageTk.PhotoImage(image1)

# label with image
l = tk.Label(root, image=photo)
l.pack()

# bind click event to image
l.bind('<Button-1>', plus(index))
l.bind('<Button-1>', on_click)


# button with image binded to the same function
#b = tk.Button(root, image=photo, command=on_click)
#b.pack()

# button with text closing window
b = tk.Button(root, text="Close", command=root.destroy)
b.pack()




# "start the engine"
root.mainloop()
from tkinter import *
import random
root = Tk()
w = 500
h = 500
r = w/2
n = 5000
dots = 0
a = Canvas(root, width=w, height=h, bg='white')
a.pack()
a.create_rectangle(0, 0, h, h, outline='blue')
a.create_oval(0, 0, h, h, outline='red')

for i in range(0, n):
    x = random.randint(0, w)
    y = random.randint(0, w)
    if (x-w/2)*(x-w/2)+(y-h/2)*(y-h/2) < r*r:
        a.create_rectangle(x, y, x, y, outline='red')
        dots += 1
    else:
        a.create_rectangle(x, y, x, y, outline='blue')
pi =4*dots/n
print(pi)
root.mainloop()

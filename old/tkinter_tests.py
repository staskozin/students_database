from tkinter import Tk, Entry

print('start')

root = Tk()

root.title = 'Жопа'

height = 5
width = 5
for i in range(height):  # Rows
    for j in range(width):  # Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)

root.mainloop()

print('end')

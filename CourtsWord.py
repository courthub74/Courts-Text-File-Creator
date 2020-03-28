from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Courts Word Pad")
root.geometry("600x600")

# Word entry field
texteditor = Text(root, width=50, height=20, font=("Times", 15))
texteditor.grid(row=0, column=0, pady=20, padx=40)


# Make the Text file function
def saveFile():
    myfile=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if myfile is None:
        return
    content = texteditor.get(1.0, 'end-1c')
    myfile.write(content)


# create text file button
button = Button(root, text='Create the Text file', width=40, height=1,
                command=saveFile)
button.grid(row=1, column=0, pady=20)

root.mainloop()



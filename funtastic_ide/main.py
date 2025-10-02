from tkinter import * 

def run_code():
    code = editor.get("1.0", END)
    exec(code)

compilor = Tk()
compilor.title("Funtastic IDE")

menu_bar = Menu(compilor)
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run_code)

# functions for the file menu 
def create_new_file():
    pass


def open_file():
    pass


def save_file():
    pass

def save_as():
    pass


# creating file menu 
file_menu = Menu(menu_bar )
file_menu.add_command(label="New", command=create_new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=compilor.quit)
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Run', menu=run_bar)
compilor.config(menu=menu_bar)


editor  = Text()
editor.pack()


compilor.mainloop()
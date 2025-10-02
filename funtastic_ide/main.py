from tkinter import * 
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import messagebox
import subprocess


#global file path 
file_path = ''

# function for storing the file path 
def set_file_path(path):
    global file_path 
    file_path = path

def run_code():
    if file_path == '':
        messagebox.showerror("Error", "Please save the file first")
        return 
    command = f"python3 {file_path}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = process.communicate()
    
    code_output.insert("1.0", output)
    code_output.insert("1.0", err)
    
compilor = Tk()
compilor.title("Funtastic IDE")

menu_bar = Menu(compilor)
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run_code)

# functions for the file menu 
def create_new_file():
    pass


def open_file():
    path = askopenfilename(filetypes=[("Python Files", "*.py"),("javascript files", "*.js"),("html files", "*.html"),("css files", "*.css")]);
    with open(path, 'r') as file:
        code = file.read()
        editor.delete("1.0", END)
        editor.insert("1.0", code)
        set_file_path(path)



def save_as():
    if file_path == '':
        path = asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"),("javascript files", "*.js"),("html files", "*.html"),("css files", "*.css")])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get("1.0", END)
        file.write(code)


# creating file menu 
file_menu = Menu(menu_bar )
file_menu.add_command(label="New", command=create_new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_as)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=compilor.quit)
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Run', menu=run_bar)
compilor.config(menu=menu_bar)


editor  = Text( wrap='word', font=('JetBrains Mono', 12))
editor.pack(expand=True, fill='both')


code_output = Text(height=10, wrap='word', font=('Fira Code', 12))
code_output.pack()
compilor.mainloop()
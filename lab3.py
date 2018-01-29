# lab 3: GUI with Tkinter, OOP
import os 
import platform
from dialog import *

# class AddStudentDialog
class AddStudentDialog(Dialog):
    
    '''
    def __init__(self, title = None, **kwargs):
        super().__init__(title, **kwargs)
    '''
    def body(self, bodyFrame):
        print("call body")
        IDLabel = tk.Label(bodyFrame, text = "Student ID")
        IDLabel.grid()
        ID = tk.StringVar()
        IDEntry = tk.Entry(bodyFrame, textvariable = ID) 
        IDEntry.grid()
    
    def validate(self):
        print("call validate")
        pass
    
    def apply(self):
        print("call apply")
        pass
    
 


 

# class MainWindow
 
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lab3")              # set title lab3
        self.resizable(True, False)     # set resizability horizontal only
        
        # create Add Label
        addLabel = tk.Label(self, text = "Add a Student")
        addLabel.grid()
  
        # create Add Button
        addButton = tk.Button(self, text = "Click to Add")
        addButton.grid(row = 0, column = 1)
          
        # create Student List Label
        StudentListLabel = tk.Label(self, text = "Student List")
        StudentListLabel.grid(row = 0, column = 2)        
        # create the scroll bar
        scrollBar = tk.Scrollbar(self)
        listBox = tk.Listbox(self, height = 3, yscrollcommand = scrollBar.set)
        listBox.grid(row = 1, column = 2)
        scrollBar.config(command = listBox.yview)
        scrollBar.grid(row = 1, column = 3)
        # set expansion for column 2
        self.columnconfigure(2, weight = 1)
        
        
        #
        countLabel = tk.Label(self, text = "Student Count: ")
        countLabel.grid(row = 1, column = 0)        

        
def main() :
    win = MainWindow()
    
    if platform.system() == 'Darwin': 
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
        os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid()))
        
    win.mainloop()

main()

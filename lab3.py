# lab 3: GUI with Tkinter, OOP
# Khang Vinh Tran

import os 
import platform
from dialog import *
from tkinter import messagebox

# class AddStudentDialog
class AddStudentDialog(Dialog):
    
    '''
    def __init__(self, title = None, **kwargs):
        super().__init__(title, **kwargs)
    '''
    def body(self, bodyFrame):
        print("call body")
        IDLabel = tk.Label(bodyFrame, text = "Student ID: ")
        IDLabel.grid(sticky = 'e')
        self.ID = tk.StringVar()
        IDEntry = tk.Entry(bodyFrame, textvariable = self.ID) 
        IDEntry.grid(row = 0, column = 1)
        
        nameLabel = tk.Label(bodyFrame, text = "Name: ")
        nameLabel.grid( sticky = 'e')
        self.name = tk.StringVar()
        nameEntry = tk.Entry(bodyFrame, textvariable = self.name) 
        nameEntry.grid(row = 1, column = 1) 
        
        languageLabel = tk.Label(bodyFrame, text = "Favorite Languge: ")
        languageLabel.grid( sticky = 'e')
        self.language = tk.StringVar()
        languageEntry = tk.Entry(bodyFrame, textvariable = self.language) 
        languageEntry.grid(row = 2, column = 1)
        
    
    def validate(self):
        print("call validate")
        if (not self.ID.get().isdigit() or len(self.ID.get()) != 3):
            print("check 1")
            return False
        elif not (self.name.get() and self.language.get()) :
            print("check 2")            
            return False
        elif (self.language.get().lower() != "python"):
            print("check 3")
            #tk.Message(self, text = "Learn Python now!!! 15 weeks can increase your knowledge by 15%").pack()
            tk.messagebox.showinfo("Learn Python Now!!!", "My friend, 15 weeks of Python can increase your networth by 15%")
        return True
            
        
    def apply(self):
        print("call apply")
        self.result = {"ID" : self.ID.get(), "Name" : self.name.get(), "Language" : self.language.get()}
    
 


 

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
        def addStudent():
            prompt = AddStudentDialog(self)
            listBox.insert(tk.END, prompt.result)

        addButton = tk.Button(self, text = "Click to Add", command = addStudent)
        addButton.grid(row = 0, column = 1)
          
        # create Student List Label
        StudentListLabel = tk.Label(self, text = "Student List")
        StudentListLabel.grid(row = 0, column = 2)  
        
        # create the scroll bar
        scrollBar = tk.Scrollbar(self)
        listBox = tk.Listbox(self, height = 3, yscrollcommand = scrollBar.set)
        # insert the item into 
        #listBox.insert(tk.END, prompt.result)
        
        listBox.grid(row = 1, column = 2, sticky = "ew")
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

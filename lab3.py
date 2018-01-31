# lab 3: GUI with Tkinter, OOP
# Khang Vinh Tran

import os 
import platform
from dialog import *
from tkinter import messagebox

# class AddStudentDialog
class AddStudentDialog(Dialog):
    
    '''
    An inheritance from dialog class
    Notice: if the inheritance's init only call its parents' init, the inheritance's init is not neccessary
    def __init__(self, title = None, **kwargs):
        super().__init__(title, **kwargs)
    '''
    
    def body(self, bodyFrame):
        """
        the body has all of the widgets
        their master is bodyFrame
        """
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
        """
        check for the three criteria of users inpt
        return False if there is any violation
        return True, otherwise
        shows appropriate error message or info message
        """
        if (not self.ID.get().isdigit() or len(self.ID.get()) != 3):
            tk.messagebox.showerror("Invalid ID", "Please enter your 3 digit student ID")
            return False
        elif not (self.name.get() and self.language.get()) :
            tk.messagebox.showerror("Empty Information", "Name and Favorite Languge can't be empty")
            return False
        elif (self.language.get().lower() != "python"):
            #tk.Message(self, text = "Learn Python now!!! 15 weeks can increase your knowledge by 15%").pack()
            tk.messagebox.showinfo("Learn Python Now!!!", "My friend, 15 weeks of Python can increase your networth by 15%")#whyy?
        return True
            
        
    def apply(self):
        """
        Overwrite the parent's apply
        store user's input into a dictionary
        """
        self.result = {"ID" : self.ID.get(), "Name" : self.name.get(), "Language" : self.language.get()}
    
 


 

# class MainWindow
 
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        """
        Create a main window with all labels
        The window has a button "Click to Add", which will invoke addStudent,
        which in turn will invoke AddStudentDialog, and update the Window's listbox 
        and show the student count
        """
        self.title("Lab3")              # set title lab3
        self.resizable(True, False)     # set resizability horizontal only
        
        # create Add Label
        addLabel = tk.Label(self, text = "Add a Student")
        addLabel.grid()
  
  
  
        # create Add Button
        addButton = tk.Button(self, text = "Click to Add", command = self.addStudent)
        addButton.grid(row = 0, column = 1)
          
        # create Student List Label
        StudentListLabel = tk.Label(self, text = "Student List")
        StudentListLabel.grid(row = 0, column = 2)  
        
        # create the scroll bar
        scrollBar = tk.Scrollbar(self)
        self.listBox = tk.Listbox(self, height = 3, yscrollcommand = scrollBar.set)
        
        self.listBox.grid(row = 1, column = 2, sticky = "ew")
        scrollBar.config(command = self.listBox.yview)
        scrollBar.grid(row = 1, column = 3, sticky = "wns")
        
        # set expansion for column 2
        self.columnconfigure(2, weight = 1)
        
        
        # count and update the number of students
        countLabel = tk.Label(self, text = "Student Count = 0")
        countLabel.grid(row = 1, column = 0) 

        


    def addStudent(self):
        """
        invoke AddStudentDialog by create an object
        If the user input is not "ok", the focus will remain on AddStudentDialog
        Otherwise, it returns an object and increment student count
        show student count on the grid
        """
        # if user input is "ok", it will return an AddStudentDialog object
        prompt = AddStudentDialog(self)
        self.listBox.insert(tk.END, prompt.result)
        
        # update the student count
        studentCount = tk.Label(self, text = "Student Count = " + str(self.listBox.size()))
        studentCount.grid(row = 1, column = 0, sticky = "w")
        
        
def main() :
    win = MainWindow()
    
    if platform.system() == 'Darwin': 
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
        os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid()))
        
    win.mainloop()

main()

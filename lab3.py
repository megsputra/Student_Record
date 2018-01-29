<<<<<<< HEAD
# lab 3: GUI with Tkinter, OOP
# Name: Mega Putra 
import tkinter as tk
import tkinter.messagebox as tkmb #for message box
import platform
import os
from dialog import *

class AddStudentDialog(dialog) :
        '''  
        def __init__(self, master, title, **kwargs):
        super(AddStudentDialog, self).__init__()  
        '''
        '''
        self._stuID_entry = tk.StringVar()
        self._stuID_entry = tk.StringVar()
        self._favLang_entry = tk.StringVar()
        self.body()
        '''
        
        def body(self, frame):
        # The body method will return a widget, and the focus will be on the returned widget.
        # Having a focus on a widget means the cursor will be at that widget.        
                self.title("Student Info")
                
                #create 3 labels
                stuID = tk.Label(self, text="Student ID")
                name = tk.Label(self, text = "Name")
                favLang = tk.Label(self, text = "Favorite Language")
                stuID.grid(row = 0, column = 0, sticky='e')
                name.grid(row = 1, column = 0, sticky='e')
                favLang.grid(row = 2, column = 0, sticky='e')
                
                #create entry boxes for the labels
                tk.Entry(self, textvariable = self._stuID_entry).grid(row = 0, column = 1)  
                tk.Entry(self, textvariable = self._name_entry).grid(row = 1, column = 1)
                tk.Entry(self, textvariable = self._favLang_entry).grid(row = 2, column = 1)   
                
                #create [OK] and [Cancel] buttons
                def okButton() : print("OK")         
                okButton = tk.Button(self, text="OK", command = okButton)
                okButton.grid(row = 4, column = 0)            
                
                def cancelButton() : print("Cancel") 
                cancelButton = tk.Button (self, text = "Cancel", command = cancelButton)
                cancelButton.grid(row = 4, column = 1)
    
    def validate(self): 
        if(self._stuID_entry != "" and self._stuID_entry.isdigit() and len(self._stuID_entry) == 3): # check studentID entry
            if self._favLang_entry != "Python" or self._favLang_entry != "python" :
                #prints mesage box
                tkmb.showinfo("Notification", "Too bad it's not Python!", parent = self)
            return True
        else:
            return False
                
        
    #def apply(self): #overriding the base class method   
        
        
# class MainWindow: 
 
def main() :
    win = AddStudentDialog()
    if platform.system() == 'Darwin': 
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
        os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid()))    
    win.mainloop()

main()
=======
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
        IDLabel = tk.Label(bodyFrame, text = "Student ID: ")
        IDLabel.grid(row = 0, column = 0)
        ID = tk.StringVar()
        IDEntry = tk.Entry(bodyFrame, textvariable = ID) 
        IDEntry.grid(row = 0, column = 1)
        
        nameLabel = tk.Label(bodyFrame, text = "Name: ")
        nameLabel.grid(row = 1, column = 0)
        name = tk.StringVar()
        nameEntry = tk.Entry(bodyFrame, textvariable = name) 
        nameEntry.grid(row = 1, column = 1) 
        
        languageLabel = tk.Label(bodyFrame, text = "Favorite Languge: ")
        languageLabel.grid(row = 2, column = 0)
        language = tk.StringVar()
        languageEntry = tk.Entry(bodyFrame, textvariable = language) 
        languageEntry.grid(row = 2, column = 1)           
    
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
        def addStudent():
            prompt = AddStudentDialog(self)        
        addButton = tk.Button(self, text = "Click to Add", command = addStudent)
        addButton.grid(row = 0, column = 1)
          
        # create Student List Label
        StudentListLabel = tk.Label(self, text = "Student List")
        StudentListLabel.grid(row = 0, column = 2)        
        # create the scroll bar
        scrollBar = tk.Scrollbar(self)
        listBox = tk.Listbox(self, height = 3, yscrollcommand = scrollBar.set)
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
>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399

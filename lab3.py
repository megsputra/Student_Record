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
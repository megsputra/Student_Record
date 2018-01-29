# CIS 41B
<<<<<<< HEAD
# Name: Mega Putra 
# Dialog window base class

#


import tkinter as tk
from abc import ABC, abstractmethod # abstact base class, a class to derive other classes from
# should never be instantiated because you dont have a body for it, empty window with buttons
# framework should be made as an abstract class
# why is MultipleInheritance bad? When/Why is this used? this is why!!!

class Dialog(tk.Toplevel, ABC):    # Multiple inheritance: Dialog gets the attributes of TopLevel and ABC
    """Base Dialog() class
       - Has standard features of a dialog box: 
          - window with [OK] and [Cancel] buttons
          - [OK] to commit a transaction, [Cancel] to cancel a transaction
       - Derived dialog boxes can be created with a small amount of customization"""

    def __init__(self, master, title=None, **kwargs):    # Q1. what is kwargs and why would this base class want to use it
=======
# Dialog window base class

import tkinter as tk
from abc import ABC, abstractmethod

class Dialog(tk.Toplevel, ABC):    # Multiple inheritance: Dialog gets the attributes of TopLevel and ABC
    """
    Base Dialog() class
       - Has standard features of a dialog box: 
          - a window with [OK] and [Cancel] buttons
          - [OK] to commit a transaction, [Cancel] to cancel a transaction
       - Derived dialog boxes can be created with a small amount of customization
    """

    def __init__(self, master, title=None, **kwargs):    # Q1. what is kwargs and why would this base class want to use it?
                                                         # kwargs means Key Word Arguemnts
                                                         # **kwargs is for unpacking keywords argument into function definition
                                                         # later on, it can be used as: for k, v in kwargs : dosomething()
>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399
        """ set up window with title, body, [OK] and [Cancel] buttons, and controls"""
        
        ABC.__init__(self)
        tk.Toplevel.__init__(self, master)  # self is Dialog, 
                                            # master is window that Dialog is spawned from, which in lab 3 is MainWindow
                                            # master needs to be passed in so that if master closes, then all spawned windows will go away

<<<<<<< HEAD
        self.grab_set()  #gives focus to a window when you have multiple windows.
        # dialog window
        # Make Dialog modal (Dialog grabs all focus, master is not active)
        self.protocol("WM_DELETE_WINDOW", self.cancel)  # Make "X" same as [Cancel] button, cancel is callback function

        self._master = master           # save master window for this Dialog instance
        #base class creates a result variable
        self.result = None              # result is *public* data that can be accessed outside the class.
                                        # result has the user input that is the result of the dialog with the user
                                        # a way to send data bac by putting it in a public variable
                                        # so you can do print(myWindow.result) - event driven
                                        
        if title:
            self.title(title)           # Q2. What does this if statement do? 

        self.v = tk.StringVar()         # Provide a generic StringVar v that can be used to store user input data for the transaction
        self.v.set('ERROR: uninitialized data')    # if a derived class wants to use v, it must set v
        
=======
        self.grab_set()                                 # Make Dialog modal (Dialog grabs all focus, master is not active)
        self.protocol("WM_DELETE_WINDOW", self.cancel)  # Make "X" same as [Cancel] button, cancel is callback function

        self._master = master           # save master window for this Dialog instance
        self.result = None              # result is *public* data that can be accessed outside the class.
                                        # result has the user input that is the result of the dialog with the user
        if title:
            self.title(title)           # Q2. What does this if statement do? 
                                        # If title is entered, set the title of self (Dialog) as what users enter

        self.v = tk.StringVar()         # Provide a generic StringVar v that can be used to store user input data for the transaction
        self.v.set('ERROR: uninitialized data')    # if a derived class wants to use v, it must set v

>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399
        bodyFrame = tk.Frame(self)                      # Create empty body frame for derived class to fill
        self.initial_focus = self.body(bodyFrame)       # Call the body() method to populate the window's body.
                                                # The body method will return a widget, and the focus will be on the returned widget.
                                                # Having a focus on a widget means the cursor will be at that widget.
<<<<<<< HEAD
                                                #             
        bodyFrame.pack(padx=5, pady=5, fill=tk.BOTH, expand='y')  

        self.buttonbox()                        # create [OK] and [Cancel] buttons as another frame
                                                # a box of two buttons
        if not self.initial_focus:              # if focus is not on a widget, then focus is Dialog 
            self.initial_focus = self           # 
=======
                                                           
        bodyFrame.pack(padx=5, pady=5, fill=tk.BOTH, expand='y')  

        self.buttonbox()                        # create [OK] and [Cancel] buttons as another frame

        if not self.initial_focus:              # if focus is not on a widget, then focus is Dialog 
            self.initial_focus = self
>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399
        self.initial_focus.focus_set()          # set the focus
        
        # Q3. Explain where the focus could be. There are 3 possibilities, with a certain precedence: first, second, third
        # List the 3 locations in order.
<<<<<<< HEAD
        # first:
        # second:
        # third: 

=======
        # first : mainWindow
        # second: dialog (prompting user to enter ID, name, language)
        # third: if the langue is not python, prompt message
        
>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399
        self.transient(master)      # Set Dialog to be transient to the master:
                                    # This means: 1. Dialog will minimize if master is minimized 
                                    # 2. Dialog causes no extra icon on taskbar
                                    # 3. Dialog appears on top of master
<<<<<<< HEAD
                                    
                                    
                                    #string format!!
=======

>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399
        self.geometry("+%d+%d" % (master.winfo_rootx()+50, master.winfo_rooty()+50)) # place Dialog window on right and down from master
        self.resizable(False,False) # Don't allow Dialog to be sizeable

        self.wait_window(self)      # Stay open until Dialog is closed by the user
<<<<<<< HEAD
    #
    #=====  methods for appearance and behavior of Dialog  =====
    # 
    
    @abstractmethod #Decorator, if anybody tries to instantiates the dialog class by itself, they will get error message
    def body(self, bodyFrame):
        """Create dialog body.  Return widget that should have initial focus."""

=======
            
            
    #
    #=====  methods for appearance and behavior of Dialog  =====
    #
    @abstractmethod
    def body(self, bodyFrame):
        """Create dialog body.  Return widget that should have initial focus."""
>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399
        raise NotImplementedError

    def buttonbox(self):
        """Add [Ok] and [Cancel] buttons]"""
<<<<<<< HEAD
        box = tk.Frame(self) # add the frame

        self.b_ok = tk.Button(box, text="OK", width=10, command=self.ok) #callback
=======
        box = tk.Frame(self)

        self.b_ok = tk.Button(box, text="OK", width=10, command=self.ok) 
>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399
        self.b_ok.pack(side=tk.LEFT, padx=5, pady=5)
        self.b_cancel = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        self.b_cancel.pack(side=tk.LEFT, padx=5, pady=5)

        if not self.initial_focus:
            self.initial_focus = self.b_cancel

        self.bind("<Return>", self.return_)        # bind() method connects a pressed key event
        self.bind("<Escape>", self.cancel)         # to a method through a callback

        box.pack()
        
    @abstractmethod
    def validate(self):
        """Return True if all dialog options are valid"""
        raise NotImplementedError        

    def ok(self, *args):
<<<<<<< HEAD
        """[Ok] button to commit change"""  
        if not self.validate():                     # if not valid
            self.initial_focus.focus_set()          # put focus back to initial focus
            return #if it doesnt return true, the ok cannot be done
=======
        """[Ok] button to commit change"""
        if not self.validate():                     # if not valid
            self.initial_focus.focus_set()          # put focus back to initial focus
            return
>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399

        self.apply()                # if everything is valid, then store input data into result
        self.cancel()               # go to close window

    def cancel(self, *args):
        """[Cancel] button to close window"""
<<<<<<< HEAD
        self._master.focus_set()    # set focus back to the master window, close top level window
=======
        self._master.focus_set()    # set focus back to the master window
>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399
        self.destroy()              # close window

    def return_(self, *args):
        """Hitting return will run the button that has focus"""
        if self.focus_get() == self.b_cancel:
            self.cancel()
        elif self.focus_get() == self.b_ok:
            self.ok()

    def apply(self):
        """set result to valid user input data"""
        self.result = self.v.get()   # result defaults to the generic StringVar v variable
                                     # If derived class handles multiple data in a data structure
                                     # then the derive class should override this method so result
                                     # can be a data structure.
<<<<<<< HEAD
        # v is from the random variable, need to get a string from a user
        # need to write this
        # need to end this with self.result = something
        
        
# Q1. what is kwargs and why would this base class want to use it        
# kwargs makes the baseclass accept any arbitrary number of arguments since we do not know how many
# arguments there are in the derived class.
# Q4. Name all the callback methods
=======

# Q4. Name all the callback methods
# body, buttonbox, validate (definition in inheritance is enfonrced), ok, cancel, return_, apply, 
>>>>>>> a79718234f7fdfd05ccdf78fc1f5bafc88a4b399

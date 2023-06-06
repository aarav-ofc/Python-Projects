# Author: Aarav Shreshth
#
# Imported modules
import tkinter as tk
import re
from tkinter import messagebox

# Signup Class
class Signup:
    def __init__(self):
        # External Path (The icon i've taken is from my pc only, if you want to use this icon, make sure to put it's correct path.)
        self.iconpath = 'F:\PY_PROJECTS\GUI App\Signup App\signup.png'

        # Window Initialization
        self.root = tk.Tk()

        #geometry
        self.root.geometry("600x400")
        self.root.minsize(width=600, height=400)
        self.root.maxsize(width=600, height=400)

        # Customization
        self.root.title("Signup App")
        self.win_icon = tk.PhotoImage(file=self.iconpath)
        self.root.iconphoto(False, self.win_icon)
        

        # Signup Title
        self.lgtitle = tk.Label(self.root, text="User Signup", font=(
            'typewriter', 30, 'bold')).pack(pady=10)
        self.lgarea = tk.Frame(self.root)

        # Name Entry
        self.name = tk.Label(self.lgarea, text="Name -",
                             font=('typewriter', 17, 'bold'))
        self.name.grid(padx=10, row=0, column=0, sticky=tk.W+tk.E)
        self.nt = tk.Entry(self.lgarea, font=(
            'typewriter', 17, 'bold'), yscrollcommand=None, width=30)
        self.nt.grid(padx=10, row=0, column=1, sticky=tk.W+tk.E)

        # Age Entry
        self.age = tk.Label(self.lgarea, text="Age -",
                            font=('typewriter', 17, 'bold'))
        self.age.grid(padx=10, row=1, column=0, sticky=tk.W+tk.E)
        self.at = tk.Entry(self.lgarea, font=(
            'typewriter', 17, 'bold'), xscrollcommand=None, yscrollcommand=None, width=30)
        self.at.grid(padx=10, row=1, column=1, sticky=tk.W+tk.E)

        # Password Entry
        self.passw = tk.Label(self.lgarea, text="Password -",
                              font=('typewriter', 17, 'bold'))
        self.passw.grid(padx=10, row=2, column=0, sticky=tk.W+tk.E)
        self.psw = tk.Entry(self.lgarea, font=(
            'typewriter', 17, 'bold'), xscrollcommand=None, yscrollcommand=None, width=30)
        self.psw.grid(padx=10, row=2, column=1, sticky=tk.W+tk.E)

        # T&C
        self.checkstate = tk.IntVar()

        self.d = tk.Checkbutton(
            self.lgarea, text="I agree to the terms and conditions of mint.", variable=self.checkstate)
        self.d.grid(pady=30, row=3, column=1, sticky=tk.W+tk.E, padx=(0, 140))

        # Signup
        self.lgbut = tk.Button(self.lgarea, text="Signup", font=(
            'typewriter', 17, 'bold'), background='black', foreground='white', command=self.signup_)
        self.lgbut.grid(padx=(0, 123), row=4, column=1, sticky=tk.W+tk.E)

        self.lgarea.pack(fill="x")
    
    # Main Execution Func.
    def signup_(self):
        # InVariables
        name = self.nt.get()
        age = self.at.get()
        password = self.psw.get()
        sizepassword = len(password)
        sizename = len(name)
        maxage = 100
        minage = 10
        special_characters = "!@#$%^&.*()-+?_=,<>\|~`{/}[]'"""

        # Checks
        #
        # For Name
        if name == "" or name == None:
            messagebox.showerror(title="Signup Error", message="Name Cannot be empty")
            return
        
        elif sizename > 15:
            messagebox.showerror(title="Signup Error", message="Name should not be more than 16 characters.")

        elif sizename < 4:
            messagebox.showerror(title="Signup Error", message="Name should not be less than 4 characters.")
        
        elif re.search("[0-9]", name) or any(c in special_characters for c in name):
            messagebox.showerror(title="Signup Error", message="Name should not contain numbers or special characters.")


        # For Age
        elif age == "":
            messagebox.showerror(title="Signup Error", message="Age Cannot be empty")
            return
        
        elif age.isnumeric() == False:
            messagebox.showerror(title="Signup Error", message="Age Cannot contain chars.")
            return
        
        elif int(age)<minage:
            messagebox.showerror(title="Signup Error", message="You are not eligible for signing up!")
            self.root.destroy()

        elif int(age)>=maxage:
            messagebox.showerror(title="Signup Error", message="Age should not be more than and equals to 100") 
        
        # For Password
        elif password == "":
            messagebox.showerror(title="Signup Error", message="Password Cannot be empty")
            return
        
        elif sizepassword < 8:
            messagebox.showerror(title="Signup Error", message=f"Password should be of atleast 8 characters, Your Password length: {sizepassword}")

            return
        
        # For T&C
        elif self.checkstate.get() == 0:
            messagebox.showerror(title="Signup Error", message="Please agree to the terms and conditions.")
            return
        
        # Successful Signup
        
        else:
            messagebox.showinfo(title="Signed Up!", message="You have successfully signed up! This signup app is made by Aarav.")
            self.root.destroy()
            
        

    # App Starter
    def start(self):
        self.root.mainloop()


app = Signup()
app.start()

# End of file


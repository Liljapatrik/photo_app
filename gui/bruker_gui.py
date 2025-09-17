from tkinter import Toplevel, Label, Button, Entry, StringVar, E, W, messagebox
from service.bruker_service import UserService

class BrukerGUI:
    def __init__(self, db, master):
        self.service = UserService(db)
        self.main_window = None
        self.master = master  

        # Tkinter StringVars
        self.main_window = None
        self.bID = StringVar()
        self.bfornavn = StringVar()
        self.betternavn = StringVar()
        self.bepost = StringVar()
        self.nybepost = StringVar()

    # Method to clear fields
    def clear_fields(self):
        self.bID.set("")
        self.bfornavn.set("")
        self.betternavn.set("")
        self.bepost.set("")
        self.nybepost.set("")

    # Main window
    def open_main_window(self):
        self.main_window = Toplevel(master=self.master)
        self.main_window.title("User")

        Label(self.main_window, text='Choose one option:').grid(row=0, column=0, padx=5, pady=10, sticky=E)

        Button(self.main_window, text='Add user', width=18, command=self.open_add_user_window).grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Button(self.main_window, text='Edit email for user', width=18, command=self.open_edit_email_window).grid(row=2, column=0, padx=5, pady=5, sticky=E)
        Button(self.main_window, text='Back', command=self.main_window.destroy).grid(row=3, column=1, padx=5, pady=25, sticky=E)

    
    # Window to add user
    def open_add_user_window(self):
        window = Toplevel()
        window.title("Add user")

        Label(window, text='Fill in the lines below:').grid(row=0, column=0, padx=5, pady=10, sticky=E)
        Label(window, text='Enter user ID: ').grid(row=1, column=0, sticky=E)
        Label(window, text='Enter First name: ').grid(row=2, column=0, sticky=E)
        Label(window, text='Enter Last name: ').grid(row=3, column=0, sticky=E)
        Label(window, text='Enter Email: ').grid(row=4, column=0, sticky=E)

        Entry(window, width=10, textvariable=self.bID).grid(row=1, column=1, sticky=W)
        Entry(window, width=20, textvariable=self.bfornavn).grid(row=2, column=1, sticky=W)
        Entry(window, width=20, textvariable=self.betternavn).grid(row=3, column=1, sticky=W)
        Entry(window, width=30, textvariable=self.bepost).grid(row=4, column=1, sticky=W)

        Button(window, text='Save', command=self.add_user).grid(row=5, column=2, sticky=E)
        Button(window, text='Back', command=window.destroy).grid(row=6, column=3, padx=5, pady=25, sticky=E)

    # Add user
    def add_user(self):
        bruker_id = self.bID.get()
        fornavn = self.bfornavn.get()
        etternavn = self.betternavn.get()
        epost = self.bepost.get()

        success, msg = self.service.add_user(bruker_id, fornavn, etternavn, epost)

        if success:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)
                
    
    # Edit email window
    def open_edit_email_window(self):
        window = Toplevel()
        window.title("Edit Email")

        Label(window, text="Fill in the lines below:").grid(row=0, column=0, padx=5, pady=10, sticky=E)
        Label(window, text="Enter user ID:").grid(row=1, column=0, sticky=E)
        Label(window, text="First name:").grid(row=2, column=0, sticky=E)
        Label(window, text="Last name:").grid(row=3, column=0, sticky=E)
        Label(window, text="Email:").grid(row=4, column=0, sticky=E)
        Label(window, text="New email:").grid(row=5, column=0, sticky=E)

        Entry(window, width=10, textvariable=self.bID).grid(row=1, column=1, padx=5, pady=5, sticky=W)
        Entry(window, width=20, state="readonly", textvariable=self.bfornavn).grid(row=2, column=1, padx=5, pady=5, sticky=W)
        Entry(window, width=20, state="readonly", textvariable=self.betternavn).grid(row=3, column=1, padx=5, pady=5, sticky=W)
        Entry(window, width=30, state="readonly", textvariable=self.bepost).grid(row=4, column=1, padx=5, pady=5, sticky=W)
        Entry(window, width=30, textvariable=self.nybepost).grid(row=5, column=1, padx=5, pady=5, sticky=W)

        Button(window, text="Find user", command=self.find_user).grid(row=1, column=2, padx=5, pady=5, sticky=E)
        Button(window, text="Save", command=self.update_email).grid(row=6, column=2, padx=5, pady=10, sticky=E)
        Button(window, text="Back", command=window.destroy).grid(row=7, column=3, padx=5, pady=25, sticky=E)

    def find_user(self):
        bruker_id = self.bID.get()
        sucess, data = self.service.get_user(bruker_id)

        if sucess:
            self.bfornavn.set(data[1])
            self.betternavn.set(data[2])
            self.bepost.set(data[3])
        else:
            messagebox.showerror("Error", data)
            self.clear_fields()

    def update_email(self):
        bruker_id = self.bID.get()
        ny_epost = self.nybepost.get()

        sucess, msg = self.service.update_email(bruker_id, ny_epost)
        if sucess:
            messagebox.showinfo("Sucess", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)
                

       
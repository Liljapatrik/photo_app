from tkinter import Toplevel, Label, Button, Entry, StringVar, Listbox, Scrollbar, VERTICAL, E, W, NS, messagebox, END
from service.emneknagg_service import EmneknaggService

class EmneknaggGUI:
    def __init__(self, db, master):
        self.service = EmneknaggService(db)
        self.master = master  

        self.main_window = None
        self.eID = StringVar()
        self.ekn = StringVar()

    def clear_fields(self):
        self.eID.set('')
        self.ekn.set('')

    # Main window
    def open_main_window(self):
        self.main_window = Toplevel(master=self.master)
        self.main_window.title("Hashtag")

        Label(self.main_window, text="Choose one option:").grid(row=0, column=0, padx=5, pady=10, sticky=E)

        Button(self.main_window, text="Add hashtag", width=20,
                command=self.open_add_window).grid(row=1, column=0, padx=5, pady=5, sticky=E)

        Button(self.main_window, text="Back", command=self.main_window.destroy).grid(row=3, column=1, padx=5, pady=25, sticky=E)
    
    def open_add_window(self):
        self.add_window = Toplevel()
        self.add_window.title("Add hashtag")

        Label(self.add_window, text="Fill in the details to add a hashtag:").grid(
            row=0, column=0, columnspan=2, padx=5, pady=10
        )

        Label(self.add_window, text="Enter hashtag ID:").grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Entry(self.add_window, width=8, textvariable=self.eID).grid(row=1, column=1, padx=5, pady=5, sticky=W)

        Label(self.add_window, text="Enter hashtag:").grid(row=2, column=0, padx=5, pady=5, sticky=E)
        Entry(self.add_window, width=20, textvariable=self.ekn).grid(row=2, column=1, padx=5, pady=5, sticky=W)

        Button(self.add_window, text="Save", command=self.save_emneknagg).grid(row=5, column=2, padx=5, pady=5, sticky=E)
        Button(self.add_window, text="Back", command=self.add_window.destroy).grid(row=6, column=3, padx=5, pady=25, sticky=E)


    # Save hashtag
    def save_emneknagg(self):
        emneknagg_id = self.eID.get()
        emneknaggen = self.ekn.get()

        success, msg = self.service.add_emneknagg(emneknagg_id, emneknaggen)

        if success:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)

        success = self.service.add_emneknagg(emneknagg_id, emneknaggen)

       

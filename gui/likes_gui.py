from tkinter import Toplevel, Label, Button, Entry, StringVar, E, W, messagebox
from service.likes_service import LikesService

class LikesGUI:
    def __init__(self, db, master):
        self.service = LikesService(db)
        self.main_window = None
        self.master = master

        # Tkinter StringVars
        self.main_window = None
        self.bildeID = StringVar()
        self.brukerID = StringVar()

    def clear_fields(self):
        self.bildeID.set("")
        self.brukerID.set("")

    # Main window
    def open_main_window(self):
        self.main_window = Toplevel(master=self.master)
        self.main_window.title("Likes")

        Label(self.main_window, text='Choose one option:').grid(row=0, column=0, padx=5, pady=10, sticky=E)

        Button(self.main_window, text='Add likes', width=10, command=self.open_add_like_window).grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Button(self.main_window, text='Delete likes', width=10, command=self.open_delete_like_window).grid(row=2, column=0, padx=5, pady=5, sticky=E)
        Button(self.main_window, text='Back', command=self.main_window.destroy).grid(row=3, column=1, padx=5, pady=25, sticky=E)

    def open_add_like_window(self):
        window = Toplevel()
        window.title("Add Like")

        Label(window, text="Enter image ID:").grid(row=1, column=0, sticky=E)
        Entry(window, width=8, textvariable=self.bildeID).grid(row=1, column=1, sticky=W)

        Label(window, text="Enter user ID:").grid(row=2, column=0, sticky=E)
        Entry(window, width=8, textvariable=self.brukerID).grid(row=2, column=1, sticky=W)

        Button(window, text="Save", command=self.add_like).grid(row=3, column=2, sticky=E)
        Button(window, text="Back", command=window.destroy).grid(row=4, column=3, padx=5, pady=25, sticky=E)

    def add_like(self):
        success, msg = self.service.add_like(self.bildeID.get(), self.brukerID.get())
        if success:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)

    def open_delete_like_window(self):
        window = Toplevel()
        window.title("Delete Like")

        Label(window, text="Enter image ID:").grid(row=1, column=0, sticky=E)
        Entry(window, width=8, textvariable=self.bildeID).grid(row=1, column=1, sticky=W)

        Label(window, text="Enter user ID:").grid(row=2, column=0, sticky=E)
        Entry(window, width=8, textvariable=self.brukerID).grid(row=2, column=1, sticky=W)

        Button(window, text="Delete", command=self.delete_like).grid(row=3, column=2, sticky=E)
        Button(window, text="Back", command=window.destroy).grid(row=4, column=3, padx=5, pady=25, sticky=E)

    def delete_like(self):
        success, msg = self.service.delete_like(self.bildeID.get(), self.brukerID.get())
        if success:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)


from tkinter import Toplevel, Label, Button, Entry, StringVar, W, E, messagebox
from service.tagForImage_service import TagForImageService

class TagForImageGUI:
    def __init__(self, db, master):
        self.service = TagForImageService(db)
        self.master = master

        # StringVar
        self.main_window = None
        self.bID = StringVar()
        self.bbeskrivelse = StringVar()
        self.bfotograf = StringVar()
        self.eID = StringVar()

    def clear_fields(self):
        self.bID.set('')
        self.bbeskrivelse.set('')
        self.bfotograf.set('')
        self.eID.set('')

    # Main window
    def open_main_window(self):
        self.window = Toplevel(master=self.master)
        self.window.title("Tag for Image")

        Label(self.window, text="Choose an option:").grid(row=0, column=0, padx=5, pady=10, sticky=E)

        Button(self.window, text="Add tag", width=10, command=self.open_add_window).grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Button(self.window, text="Delete tag", width=10, command=self.open_delete_window).grid(row=2, column=0, padx=5, pady=5, sticky=E)
        Button(self.window, text="Back", command=self.window.destroy).grid(row=3, column=1, padx=5, pady=25, sticky=E)

    # Add tag
    def open_add_window(self):
        self.clear_fields()
        self.add_window = Toplevel()
        self.add_window.title("Add tag")

        Label(self.add_window, text="Fill in the details:").grid(row=0, column=0, padx=5, pady=10, sticky=E)
        Label(self.add_window, text="Image ID:").grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Label(self.add_window, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky=E)
        Label(self.add_window, text="Photographer:").grid(row=3, column=0, padx=5, pady=5, sticky=E)
        Label(self.add_window, text="Hashtag ID:").grid(row=4, column=0, padx=5, pady=20, sticky=E)

        Entry(self.add_window, width=8, textvariable=self.bID).grid(row=1, column=1, padx=5, pady=5, sticky=W)
        Entry(self.add_window, width=20, state='readonly', textvariable=self.bbeskrivelse).grid(row=2, column=1, padx=5, pady=5, sticky=W)
        Entry(self.add_window, width=8, state='readonly', textvariable=self.bfotograf).grid(row=3, column=1, padx=5, pady=5, sticky=W)
        Entry(self.add_window, width=8, textvariable=self.eID).grid(row=4, column=1, padx=5, pady=20, sticky=W)

        Button(self.add_window, text="Find Image", command=self.find_image).grid(row=1, column=2, padx=5, pady=5, sticky=W)
        Button(self.add_window, text="Save", command=self.add_tag).grid(row=5, column=2, padx=5, pady=5, sticky=W)
        Button(self.add_window, text="Back", command=self.add_window.destroy).grid(row=6, column=3, padx=5, pady=25, sticky=E)

    def find_image(self):
        success, result = self.service.get_image_info(self.bID.get())
        if success:
            self.bbeskrivelse.set(result[1])
            self.bfotograf.set(result[2])
        else:
            messagebox.showerror("Error", result)
            self.bbeskrivelse.set('')
            self.bfotograf.set('')

    def add_tag(self):
        if not self.bID.get() or not self.eID.get():
            messagebox.showwarning("Error", "Image ID and Hashtag ID must be entered")
            return
        success, msg = self.service.add_tag(self.bID.get(), self.eID.get())
        if success:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)

    # Radera tag
    def open_delete_window(self):
        self.clear_fields()
        self.delete_window = Toplevel()
        self.delete_window.title("Delete tag")

        Label(self.delete_window, text="Fill in the details:").grid(row=0, column=0, padx=5, pady=10, sticky=E)
        Label(self.delete_window, text="Image ID:").grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Label(self.delete_window, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky=E)
        Label(self.delete_window, text="Photographer:").grid(row=3, column=0, padx=5, pady=5, sticky=E)
        Label(self.delete_window, text="Hashtag ID:").grid(row=4, column=0, padx=5, pady=20, sticky=E)

        Entry(self.delete_window, width=8, textvariable=self.bID).grid(row=1, column=1, padx=5, pady=5, sticky=W)
        Entry(self.delete_window, width=20, state='readonly', textvariable=self.bbeskrivelse).grid(row=2, column=1, padx=5, pady=5, sticky=W)
        Entry(self.delete_window, width=8, state='readonly', textvariable=self.bfotograf).grid(row=3, column=1, padx=5, pady=5, sticky=W)
        Entry(self.delete_window, width=8, textvariable=self.eID).grid(row=4, column=1, padx=5, pady=20, sticky=W)

        Button(self.delete_window, text="Find Image", command=self.find_image).grid(row=1, column=2, padx=5, pady=5, sticky=W)
        Button(self.delete_window, text="Delete Tag", command=self.delete_tag).grid(row=5, column=2, padx=5, pady=5, sticky=W)
        Button(self.delete_window, text="Back", command=self.delete_window.destroy).grid(row=6, column=3, padx=5, pady=25, sticky=E)

    def delete_tag(self):
        if not self.bID.get() or not self.eID.get():
            messagebox.showwarning("Error", "Image ID and Hashtag ID must be entered")
            return
        success, msg = self.service.delete_tag(self.bID.get(), self.eID.get())
        if success:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)

    
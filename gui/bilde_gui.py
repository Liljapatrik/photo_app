from tkinter import Toplevel, Button, Label, Entry, StringVar, E, W, messagebox
from service.bilde_service import BildeService  

class BildeGUI:
    def __init__(self, db, master):
        self.db = db
        self.service = BildeService(db)
        self.master = master  

        self.main_window = None
        self.bID = StringVar()
        self.bbeskrivelse = StringVar()
        self.bdato = StringVar()
        self.bfotograf = StringVar()
        self.ny_beskrivelse = StringVar()

    # Method to clear fields
    def clear_fields(self):
        self.bID.set("")
        self.bbeskrivelse.set("")
        self.bdato.set("")
        self.bfotograf.set("")
        self.ny_beskrivelse.set("")

     # Main window
    def open_main_window(self):
        self.main_window = Toplevel(master=self.master)
        self.main_window.title("Image")

        # Label
        Label(self.main_window, text='Choose one option:').grid(row=0, column=0, padx=5, pady=10, sticky=E)

        # Buttons
        Button(self.main_window, text='Add image', width=18, command=self.open_add_image_window).grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Button(self.main_window, text='Edit description', width=18, command=self.open_edit_description_window).grid(row=2, column=0, padx=5, pady=5, sticky=E)
        Button(self.main_window, text='Delete image', width=18, command=self.open_delete_image_window).grid(row=3, column=0, padx=5, pady=5, sticky=E)
        Button(self.main_window, text='Back', command=self.main_window.destroy).grid(row=4, column=1, padx=5, pady=25, sticky=E)

    # Window to add image
    def open_add_image_window(self):
        window = Toplevel()
        window.title("Add Image")

        Label(window, text='Enter Image ID:').grid(row=1, column=0, sticky=E)
        Label(window, text='Enter Description:').grid(row=2, column=0, sticky=E)
        Label(window, text='Enter Date (YYYY-MM-DD):').grid(row=3, column=0, sticky=E)
        Label(window, text='Enter Photographer ID:').grid(row=4, column=0, sticky=E)

        Entry(window, width=8, textvariable=self.bID).grid(row=1, column=1, sticky=W)
        Entry(window, width=20, textvariable=self.bbeskrivelse).grid(row=2, column=1, sticky=W)
        Entry(window, width=10, textvariable=self.bdato).grid(row=3, column=1, sticky=W)
        Entry(window, width=8, textvariable=self.bfotograf).grid(row=4, column=1, sticky=W)

        Button(window, text='Save', command=self.add_image).grid(row=5, column=2, sticky=E)
        Button(window, text='Back', command=window.destroy).grid(row=6, column=3, padx=5, pady=25, sticky=E)
    
    # Add image
    def add_image(self):
        bilde_id = self.bID.get()
        beskrivelse = self.bbeskrivelse.get()
        dato = self.bdato.get()
        fotograf = self.bfotograf.get()

        success, msg = self.service.add_image(bilde_id, beskrivelse, dato, fotograf)
        if success:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)

    # Edit description window
    def open_edit_description_window(self):
        window = Toplevel()
        window.title("Edit Description")

        Label(window, text='Image ID:').grid(row=1, column=0, sticky=E)
        Label(window, text='Current description:').grid(row=2, column=0, sticky=E)
        Label(window, text='Date:').grid(row=3, column=0, sticky=E)
        Label(window, text='Photographer:').grid(row=4, column=0, sticky=E)
        Label(window, text='New description:').grid(row=5, column=0, sticky=E)

        Entry(window, width=8, textvariable=self.bID).grid(row=1, column=1, sticky=W)
        Entry(window, width=20, textvariable=self.bbeskrivelse, state="readonly").grid(row=2, column=1, sticky=W)
        Entry(window, width=10, textvariable=self.bdato, state="readonly").grid(row=3, column=1, sticky=W)
        Entry(window, width=8, textvariable=self.bfotograf, state="readonly").grid(row=4, column=1, sticky=W)
        Entry(window, width=20, textvariable=self.ny_beskrivelse).grid(row=5, column=1, sticky=W)

        Button(window, text='Find', command=self.find_image).grid(row=1, column=2, padx=5, pady=5, sticky=E)
        Button(window, text='Save', command=self.update_description).grid(row=6, column=2, padx=5, pady=5, sticky=E)
        Button(window, text='Back', command=window.destroy).grid(row=7, column=3, padx=5, pady=25, sticky=E)


    def find_image(self):
        bilde_id = self.bID.get()
        sucess, result = self.service.find_image_by_id(bilde_id)

        if sucess:
            self.bbeskrivelse.set(result[1])
            self.bdato.set(result[2])
            self.bfotograf.set(result[3])
        else:
            messagebox.showerror("Error", result)
            self.clear_fields()

    def update_description(self):
        bilde_id = self.bID.get()
        ny_beskrivelse = self.ny_beskrivelse.get()

        sucess, msg = self.service.update_description(bilde_id, ny_beskrivelse)

        if sucess:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)

    def open_delete_image_window(self):
        window = Toplevel()
        window.title("Delete Image")

        Label(window, text='Image ID:').grid(row=1, column=0, sticky=E)
        Entry(window, width=8, textvariable=self.bID).grid(row=1, column=1, sticky=W)

        Button(window, text='Delete', command=self.delete_image).grid(row=2, column=2, padx=5, pady=5, sticky=E)
        Button(window, text='Back', command=window.destroy).grid(row=3, column=3, padx=5, pady=25, sticky=E)

    def delete_image(self):
        success, msg = self.service.delete_image(self.bID.get())
            
        if success:
                messagebox.showinfo("Success", msg)
                self.clear_fields()
        else:
            messagebox.showerror("Error", msg)
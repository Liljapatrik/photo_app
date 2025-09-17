from tkinter import Toplevel, Label, Button, Entry, StringVar, Listbox, Scrollbar, VERTICAL, E, W, NS, messagebox, END
from service.kommentar_service import KommentarService

class KommentarGUI:
    def __init__(self, db, master):
        self.service = KommentarService(db)
        self.master = master  

        self.main_window = None
        self.bID = StringVar()
        self.brID = StringVar()
        self.bkommentar = StringVar()
        self.bbeskrivelse = StringVar()
        self.bdato = StringVar()

        self.bfornamn = StringVar()
        self.befternamn = StringVar()

    # Clean field
    def clear_fields(self):
        self.bID.set('')
        self.brID.set('')
        self.bkommentar.set('')
        self.bbeskrivelse.set('')
        self.bdato.set('')
        self.bfornamn.set('')
        self.befternamn.set('')

    # Main window
    def open_main_window(self):
        window = Toplevel(master=self.master)
        window.title("Comments")

        Label(window, text="Choose one option").grid(row=0, column=0, padx=5, pady=10, sticky=E)

        Button(window, text="Add comment", width=30, command=self.open_add_comment_window).grid(row=1, column=0, padx=5, pady=5)
        Button(window, text="Delete comment", width=30, command=self.open_delete_comment_window).grid(row=2, column=0, padx=5, pady=5)
        Button(window, text="Comments per image", width=30, command=self.open_comments_by_image_window).grid(row=3, column=0, padx=5, pady=5)
        Button(window, text="Comments overview", width=30, command=self.open_comments_overview_window).grid(row=4, column=0, padx=5, pady=5)
        Button(window, text="Back", command=lambda: [self.clear_fields(), window.destroy()]).grid(row=5, column=1, padx=5, pady=25, sticky=E)

    # Window to add comment
    def open_add_comment_window(self):
        window = Toplevel()
        window.title("Add comment")

        # User ID
        Label(window, text="User ID:").grid(row=0, column=0, sticky=E)
        Entry(window, width=10, textvariable=self.bID).grid(row=0, column=1, sticky=W)

        # Description (readonly)
        Label(window, text="Description:").grid(row=1, column=0, sticky=E)
        Entry(window, width=30, textvariable=self.bbeskrivelse, state='readonly').grid(row=1, column=1, sticky=W)

        # Uploaded date (readonly)
        Label(window, text="Uploaded datue:").grid(row=2, column=0, sticky=E)
        Entry(window, width=15, textvariable=self.bdato, state='readonly').grid(row=2, column=1, sticky=W)

        # User ID
        Label(window, text="User ID:").grid(row=3, column=0, sticky=E)
        Entry(window, width=10, textvariable=self.brID).grid(row=3, column=1, sticky=W)

        # Comment
        Label(window, text="Comment:").grid(row=4, column=0, sticky=E)
        Entry(window, width=40, textvariable=self.bkommentar).grid(row=4, column=1, sticky=W)

        # Buttons
        Button(window, text="Search image", command=self.search_image).grid(row=0, column=2, padx=5)
        Button(window, text="Add comment", command=self.add_comment).grid(row=5, column=2, sticky=E)
        Button(window, text="Back", command=lambda: [self.clear_fields(), window.destroy()]).grid(row=7, column=3, padx=5, pady=25, sticky=E)

    # Method to get imageinfo
    def search_image(self):
        success, result = self.service.get_image_info(self.bID.get())
        if success:
            self.bbeskrivelse.set(result[1])
            self.bdato.set(result[2])
        else:
            messagebox.showinfo("Info", result)
            self.bbeskrivelse.set('')
            self.bdato.set('')

    # Add comment
    def add_comment(self):
        success, msg = self.service.add_comment(
            self.bID.get(), self.brID.get(), self.bkommentar.get()
        )
        if success:
            messagebox.showinfo("Success", msg)
            self.clear_fields()
        else:
            messagebox.showerror("Error", msg)

    def open_delete_comment_window(self):
        window = Toplevel()
        window.title("Delete comment")

        # Labels och Entries
        Label(window, text="Serach for image ID:").grid(row=0, column=0, sticky=E, padx=5, pady=5)
        Entry(window, textvariable=self.bID).grid(row=0, column=1, sticky=W, padx=5, pady=5)

        Label(window, text="User ID:").grid(row=2, column=6, sticky=E, padx=5, pady=5)
        Entry(window, textvariable=self.brID, state="readonly").grid(row=2, column=5, sticky=W, padx=5, pady=5)

        # Listbox + scrollbar
        self.lst_kommentar = Listbox(window, width=50, height=10)
        self.lst_kommentar.grid(row=1, column=0, columnspan=2, rowspan=10, padx=5, pady=5, sticky=W+E)

        y_scroll = Scrollbar(window, orient=VERTICAL, command=self.lst_kommentar.yview)
        y_scroll.grid(row=2, column=2, rowspan=10, sticky=NS, padx=(0,5), pady=(0,5))
        self.lst_kommentar.config(yscrollcommand=y_scroll.set)

        # Bind to see user ID
        self.lst_kommentar.bind("<<ListboxSelect>>", self.on_comment_select)

        # Buttons
        Button(window, text="Search", command=self.search_comments).grid(row=0, column=2, padx=5, pady=5)
        Button(window, text="Delete chosen comment", command=self.delete_selected).grid(row=12, column=5, padx=5, pady=10, sticky=W)
        Button(window, text="Back", command=lambda: [self.clear_fields(), window.destroy()]).grid(row=13, column=6, padx=5, pady=10)

    # Search for comment
    def search_comments(self):
        self.lst_kommentar.delete(0, END)
        success, comment = self.service.get_comments_by_image(self.bID.get())

        if not success:
            messagebox.showinfo("info", comment)
            return
        
        for com in comment:
            self.lst_kommentar.insert(END, com)

    # When a comment has been marked 
    def on_comment_select(self, event):
        selection = self.lst_kommentar.curselection()
        if not selection:
            return

        kommentar = self.lst_kommentar.get(selection[0])
        # Get user info
        success, user_info = self.service.get_user_info_by_comment(kommentar)

        if success:
            self.brID.set(user_info[0])
            self.bfornamn.set(user_info[1])
            self.befternamn.set(user_info[2])
        else:
            self.brID.set("")
            self.bfornamn.set("")
            self.befternamn.set("")

    # Delete choosen comment
    def delete_selected(self):
        selection = self.lst_kommentar.curselection()
        if not selection:
            messagebox.showinfo("Info", "No comment selected.")
            return
        comment = self.lst_kommentar.get(selection[0])
        success, msg = self.service.delete_comment(self.bID.get(), self.brID.get(), comment)

        if success:
            messagebox.showinfo("Deleted", msg)
            # Update the list
            self.search_comments()
            self.brID.set("")
            self.bID.set("")
        else:
            messagebox.showerror("Error", msg)


    # Main window for comment per user
    def open_comments_by_image_window(self):
        window = Toplevel()
        window.title("Comments on image")

        # Labels
        Label(window, text="Search image ID:").grid(row=0, column=0, padx=5, pady=5, sticky=E)
        Label(window, text="First name:").grid(row=4, column=3, padx=5, pady=5, sticky=E)
        Label(window, text="Last name:").grid(row=5, column=3, padx=5, pady=5, sticky=E)
        Label(window, text="Comments:").grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Entry
        Entry(window, width=8, textvariable=self.bID).grid(row=0, column=1, padx=5, pady=5, sticky=W)
        Entry(window, width=15, state="readonly", textvariable=self.bfornamn).grid(row=4, column=4, padx=5, pady=5, sticky=W)
        Entry(window, width=20, state="readonly", textvariable=self.befternamn).grid(row=5, column=4, padx=5, pady=5, sticky=W)

        # Listbox + Scrollbar
        self.lst_kommentar = Listbox(window, width=50, height=10)
        self.lst_kommentar.grid(row=2, column=1, rowspan=10, padx=(100,0), pady=5, sticky=E)
        y_scroll = Scrollbar(window, orient=VERTICAL, command=self.lst_kommentar.yview)
        y_scroll.grid(row=2, column=2, rowspan=10, sticky=NS, pady=5)
        self.lst_kommentar.config(yscrollcommand=y_scroll.set)

        # Bind selection to view userinfo
        self.lst_kommentar.bind("<<ListboxSelect>>", self.on_comment_select)

        # Buttons
        Button(window, text="Search", command=self.search_comments).grid(row=0, column=2, padx=5)
        Button(window, text="Back", command=lambda: [self.clear_fields(), window.destroy()]).grid(row=13, column=6, padx=5, pady=25, sticky=E)


    # Comments overview window
    def open_comments_overview_window(self):
            
        self.window_overview = Toplevel()
        self.window_overview.title('Overview over comments')

        # Labels
        Label(self.window_overview, text='Search user ID:').grid(row=0, column=0, padx=5, pady=5, sticky=E)
        Label(self.window_overview, text='Choose on description to get an overview over comments for an image:').grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Entry for user ID
        Entry(self.window_overview, width=10, textvariable=self.brID).grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Listbox + scrollbar
        self.lst_bilde = Listbox(self.window_overview, width=50, height=20)
        self.lst_bilde.grid(row=2, column=1, rowspan=10, padx=(100,0), pady=5, sticky=E)

        y_scroll = Scrollbar(self.window_overview, orient=VERTICAL, command=self.lst_bilde.yview)
        y_scroll.grid(row=2, column=3, rowspan=10, padx=(0,5), pady=5, sticky=NS)
        self.lst_bilde.config(yscrollcommand=y_scroll.set)

        # Bind selection to show comments when a image marks.
        self.lst_bilde.bind('<<ListboxSelect>>', self.on_bilde_select)

        # Buttons
        Button(self.window_overview, text='Search', command=self.search_user_bilder).grid(row=0, column=2, padx=5, pady=5, sticky=W)
        Button(self.window_overview, text='Back', command=self.window_overview.destroy).grid(row=12, column=4, padx=5, pady=25, sticky=E)

    # Method to serach for images for an user.
    def search_user_bilder(self):
        success, image = self.service.get_bilder_by_user(self.brID.get())
        # Clean list first
        self.lst_bilde.delete(0, END)

        if success:
            for description in image:
                self.lst_bilde.insert(END, description)
        else:
            messagebox.showinfo("Info", image)

    # Method when a image marks in the listbox
    def on_bilde_select(self, event):
        if not self.lst_bilde.curselection():
            return

        description = self.lst_bilde.get(self.lst_bilde.curselection()[0])
        success, comments = self.service.get_comments_by_beskrivelse(description)
        if success:
            self.show_kommentarer(comments)
        else:
            messagebox.showinfo("Info", comments)

    # Show comments in a new window
    def show_kommentarer(self, kommentarer):
        vindu_kommentarer = Toplevel()
        vindu_kommentarer.title('Comments for image')

        Label(vindu_kommentarer, text='Comments for image:').grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lst_kommentarer = Listbox(vindu_kommentarer, width=40, height=20)
        lst_kommentarer.grid(rowspan=10, column=1, padx=(0,100), pady=5)

        for kommentar in kommentarer:
            lst_kommentarer.insert(END, kommentar)

        Button(vindu_kommentarer, text='Back', command=vindu_kommentarer.destroy).grid(row=11, column=3, padx=5, pady=25, sticky=E)






    
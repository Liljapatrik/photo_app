from tkinter import Tk, Button, Label
from database import Database

from gui.bruker_gui import BrukerGUI
from gui.bilde_gui import BildeGUI
from gui.likes_gui import LikesGUI
from gui.kommentar_gui import KommentarGUI
from gui.emneknagg_gui import EmneknaggGUI
from gui.tagForImage_gui import TagForImageGUI

class MainMenu:
    def __init__(self, db):
        # Connect to the database
        self.db = db
        # Main window
        self.root = Tk()
        self.root.title("Meny")

        # Label 
        self.lbl = Label(self.root, text="Choose one option from the menu")
        self.lbl.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        # User
        self.user_btn = Button(self.root, text="User", width=10, command=self.open_user_window)
        self.user_btn.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        # Image
        self.image_btn = Button(self.root, text="Image", width=10, command=self.open_image_window)
        self.image_btn.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        # Likes 
        self.likes_btn = Button(self.root, text="Likes", width=10, command=self.open_like_window)
        self.likes_btn.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        # Comments
        self.comments_btn = Button(self.root, text="Comments", width=10, command=self.open_comment_window)
        self.comments_btn.grid(row=4, column=0, padx=5, pady=5, sticky="e")

        # Hashtags
        self.hashtags_btn = Button(self.root, text="Hashtags", width=10, command=self.open_hashtag_window)
        self.hashtags_btn.grid(row=5, column=0, padx=5, pady=5, sticky="e")

        #TagForImage
        self.tagForBilde_btn = Button(self.root, text="TagForImage", width=10, command=self.open_tagForImage_window)
        self.tagForBilde_btn.grid(row=6, column=0, padx=5, pady=5, sticky="e")

        # Button to close the window
        self.close_btn = Button(self.root, text="Close", command=self.root.destroy)
        self.close_btn.grid(row=7, column=1, padx=5, pady=25, sticky="e")

    # Start Tkinter loop
    def run(self):
        self.root.mainloop()

    # Open user window
    def open_user_window(self):
        bruker_gui = BrukerGUI(self.db, master=self.root)
        bruker_gui.open_main_window()

    def open_image_window(self):
        bilde_gui = BildeGUI(self.db, master=self.root)
        bilde_gui.open_main_window()

    def open_like_window(self):
        likes_gui = LikesGUI(self.db, master=self.root)
        likes_gui.open_main_window()

    def open_comment_window(self):
        kommentar_gui = KommentarGUI(self.db, master=self.root)
        kommentar_gui.open_main_window()

    def open_hashtag_window(self):
        emneknagg_gui = EmneknaggGUI(self.db, master=self.root)
        emneknagg_gui.open_main_window()

    def open_tagForImage_window(self):
        tagForImage_gui = TagForImageGUI(self.db, master=self.root)
        tagForImage_gui.open_main_window()

# Run the application
if __name__ == "__main__":
    db = Database()
    app = MainMenu(db)
    app.run()
    db.close()
                        
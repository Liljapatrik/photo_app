# Photo Application
This is a Python-based desktop application for managing users, photos, comments, likes hashtags, and tags. The app uses Tkinter for the GUI and a relational database (MySQL) in the backend.

## Tech Stack
- Python
- Tkinter
- MySQL

## Features
### User Management
- Add users
- Edit information from a user

### Photo Management
- Add, update and delete photos
- View photo details (description, photographer)

### Comment Management
- Add and delete comments
- List of comments for an user
- List of comments for an image 

### Likes Management
- Add like from users on photos
- Remove likes

### Hashtag Management
- Add and remove hashtags
- Tag photos with hashtags

### Tag Management
- Add and delete tags 

## Project Structure
photo_app/
│
├── gui/                    # GUI classes (Tkinter)
│   ├── bilde_gui.py        # Photo management   
│   ├── bruker_gui.py       # User management     
│   ├── emneknagg_gui.py    # Hashtag management 
│   ├── kommentar_gui.py    # Comment management    
│   ├── like_gui.py         # Likes management 
│   └── tagForImage_gui.py  # Tag photos with hashtags    
│
├── service/                # Business logic
│   ├── bilde_service.py
│   ├── bruker_service.py
│   ├── kommentar_service.py
│   ├── hashtag_service.py
│   ├── like_service.py
│   └── tagForImage_service.py
│
├── database/               # Database connection
│   └── database.py
│
├── main.py                 # Entry point
└── README.md               # Documentation

## Installation
###  Requirements
- Python 
- Dependencies:
```bash
pip install mysql-connector-python
```

### Database Setup
1. Create a MySQL database.
2. Run the provided SQL scripts to create the tables:
    - Bilde
    - Bruker
    - Likes
    - Kommentar
    - Emneknagg (Hashtag)
    - TagForBilde (TagForImage)
3. Configure the connection in database.py:
```bash
self.connection = mysql.connector.connect(
    host="localhost"
    user="your_username"
    password="your_password"
    database="photo_db"
)
```

### Running the Application
From the project root:
```bash
python main.py
```
This will open the main GUI window where you can navigate between the features. 

### Example Workflow
1. Add a new photo in Photo GUI.
2. Link a hashtag to the photo in TagForImage GUI.
3. Like the photo in Like GUI

## Screenshots
Below are some screenshots showing the main features of the application.

### Main Menu
Main menu where the user can navigate between different features. 
![Main menu](images/menu.png)

### User
User menu where the user can choose between add and edit user.
![User menu](images/userMenu.png)

#### Add User
1. Enter user id, name and email to add an user.
![Add user](images/addUser1.png)
2. If user id already exists an error message shows up.
![Add user](images/addUser2.png)
3. A messagebox "user added successfully" when a user is added
![Add user](images/addUser3.png)

#### Update Email For User
1. Enter id to find user. If successful name and email shows up in the readonly field. 
![Update user](images/updateUser1.png)
2. Write a new email. If successful an showinfo messagebox appears. 
![Update user](images/updateUser2.png)

### Image
Image menu where the user can choose between add, edit and delete image. 
![Image menu](images/imageMenu.png)

#### Add Image
1. Fill in all fields to add an image
![Add image](images/addImage1.png)
2. Messagebox shows up when an image has been added. 
![Add image](images/addImage2.png)
3. If image id already exists it will cause an error.
![Add image](images/addImage3.png)
3. If photographer (foreign key to user id) does not exist it will cause error. 
![Add image](images/addImage4.png)

#### Update description on an image
1. Enter image id to get description and date.
![Update image](images/editImage1.png)
2. Enter the new description for the image. A success messagebox appears.
![Update image](images/editImage2.png)

#### Delete an image
1. Image successfully deleted
![Delete image](images/deleteImage1.png)
2. Error when the image id does not exist.
![Delete image](images/deleteImage2.png)

### Likes
Likes menu for add and delete likes.
![Like menu](images/likeMenu.png)

#### Add Like
1. Like added. 
![Add like](images/addLike1.png)
2. Error if a like already exists. 
![Add like](images/addLike2.png)

#### Delete Like
1. Like successfully deleted
![Delete like](images/deleteLike.png)
2. Error if image id or user id does not exist. 
![Delete like](images/deleteLike2.png)
![Delete like](images/deleteLike3.png)

### Comments
Comment menu where user can add, delete and get an overview over comments.
![Comment menu](images/commentMenu.png)

#### Add Comment
1. Enter user id to get image-description and date.
![Add comment](images/addComment.png)
2. Comment added successfully. 
![Add comment](images/addComment2.png)

#### Delete Comment
1. Enter image id to get comments on the image.
![Delete comment](images/deleteComment.png)
2. Choose which comment should be deleted and user id appears. 
![Delete comment](images/deleteComment2.png)
3. Comment successfully deleted 
![Delete comment](images/deleteComment3.png)

#### Comments per Image
1. Enter user id to get comments
![Comments per image](images/commentImage1.png)
2. Choose one comment to get information about the user.
![Comments per image](images/commentImage2.png)
#### Comments Overview
1. Enter user id and the user gets all the images for the given user.
![Comment overview](images/commentOverview1.png)
2. If the user chooses an image-description, a popup window appears with all the comments of a image. 
![Comment overview](images/commentOverview2.png)

### Hashtags
Hashtag menu where the user can add hashtag. 
![Hashtag menu](images/hashtagMenu.png)

#### Add Hashtag
1. Hashtag successfully added.
![Add hashtag](images/addHashtag1.png)
2. Error if the hashtag already exists. 
![Add hashtag](images/addHashtag2.png)

### Tags
Tag menu where the user can add and delete tags.
![Tag menu](images/tagMenu.png)

#### Add tag
1. Enter image id to get information about the image.
![Add tag](images/addTag1.png)
2. Enter hashtag id to add hashtag.
![Add tag](images/addTag2.png)
3. Error if hashtag already exists. 
![Add tag](images/addTag3.png)

#### Delete tag
Enter image id and the hashtag to delete a hashtag. 
![Delete tag](images/deleteTag.png)

## Future Improvements
There are several areas where the application can be further develop:

- **Improved user experience** - make the GUI more intuitive and user-friendly. 
- **Auto generated IDs** - implement automatic ID generation for primary keys instead of manual entry.
- **Better error handling** - provide more detailed and user-friendly error messages.
- **Database enhancements** - extend the schema to support more advamdes features and relationships.

## Summary
This project demonstrates how a Python desktop application can integrate a graphical user interface (GUI) with a relational database backend. The application covers a wide range of functionality, including user management, photos, comments, likes, hashtags, and tags. It follows a layered structure with clear separation between the GUI (Tkinter), business logic (services), and database access, making the project easier to maintain and extend.  

## Highlights
One part of this project that I am particularly proud of is how the database and application logic have been connected:  

- **SQL setup and relationships** – the database schema is carefully designed with primary/foreign keys to ensure proper relationships between tables.   
- **Business logic layer** – services handle validation and interaction between the GUI and database, ensuring clean separation of concerns.  
- **GUI integration** – Tkinter interfaces are directly connected to the business logic, making it possible to manage data in a user-friendly way while maintaining the backend.  

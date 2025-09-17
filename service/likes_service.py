from database import Database

class LikesService:
    def __init__(self, db: Database):
         self.db = db

    # Method to see if bilde ID exists 
    def _bilde_exists(self, cursor, bilde_id):
        cursor.execute(
              "SELECT COUNT(*) FROM Bilde WHERE BildeID=%s", 
              (bilde_id,)
        )
        return cursor.fetchone()[0] > 0
    
    # Method to see if user ID exists 
    def _bruker_exists(self, cursor, bruker_id):
        cursor.execute(
             "SELECT COUNT(*) FROM Bruker WHERE BrukerID=%s", 
             (bruker_id,)
        )
        return cursor.fetchone()[0] > 0
    
    # Method to see if like exists 
    def _like_exists(self, cursor, bilde_id, bruker_id):
        cursor.execute(
             "SELECT COUNT(*) FROM Likes WHERE BildeID=%s AND BrukerID=%s", 
             (bilde_id, bruker_id)
        )
        return cursor.fetchone()[0] > 0
    
    # Add like 
    def add_like(self, bilde_id, bruker_id):
            if not bilde_id or not bruker_id:
                 return False, "Both image ID and user ID are required."
            
            cursor = self.db.get_cursor()
            try:
                if not self._bilde_exists(cursor, bilde_id):
                    return False, "Image ID not found."
                if not self._bruker_exists(cursor, bruker_id):
                    return False, "User ID not found."
                if self._like_exists(cursor, bilde_id, bruker_id):
                     return False, "Like already exist for image and user."
                     
                cursor.execute(
                     "INSERT INTO Likes (BildeID, BrukerID) VALUES (%s, %s)", 
                     (bilde_id, bruker_id)
                )
                self.db.commit()
                return True, "Like added successfully."
            except Exception as e:
                 self.db.rollback()
                 return False, f"Error adding like: {e}"
            finally:
                 cursor.close()

    # Delete like
    def delete_like(self, bilde_id, bruker_id):
            if not bilde_id or not bruker_id:
                 return False, "Both image ID and user ID are required."
            
            cursor = self.db.get_cursor()
            try:
                if not self._bilde_exists(cursor, bilde_id):
                    return False, "Image ID not found."
                if not self._bruker_exists(cursor, bruker_id):
                    return False, "User ID not found."
                if not self._like_exists(cursor, bilde_id, bruker_id):
                    return False, "Like not found for image and user."
                 
                # Delete like
                cursor.execute(
                     "DELETE FROM Likes WHERE BildeID=%s AND BrukerID=%s", 
                     (bilde_id, bruker_id)
                )
                self.db.commit()
                return True, "Like deleted successfully."
            except Exception as e:
                 self.db.rollback()
                 return False, f"Error deleting like: {e}"
            finally:
                 cursor.close()
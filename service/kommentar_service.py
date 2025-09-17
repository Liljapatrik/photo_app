from database import Database

class KommentarService:
    def __init__(self, db: Database):
        self.db = db

    # Check if image exists
    def _bilde_exists(self, cursor, bilde_id):
        cursor.execute(
            "SELECT COUNT(*) FROM Bilde WHERE BildeID=%s", 
            (bilde_id,)
        )
        return cursor.fetchone()[0] > 0

    # Check if user exists
    def _bruker_exists(self, cursor, bruker_id):
        cursor.execute(
            "SELECT COUNT(*) FROM Bruker WHERE BrukerID=%s", 
            (bruker_id,)
        )
        return cursor.fetchone()[0] > 0

    # Check if comment exists 
    def _comment_exists(self, cursor, bilde_id, bruker_id, kommentar):
        cursor.execute(
            "SELECT COUNT(*) FROM Kommentar WHERE BildeID=%s AND BrukerID=%s AND Kommentaren=%s",
            (bilde_id, bruker_id, kommentar)
        )
        return cursor.fetchone()[0] > 0
    
    # Get image info
    def get_image_info(self, bilde_id):
        cursor = self.db.get_cursor()
        try:
            cursor.execute(
                "SELECT BildeID, Beskrivelse, OpplastetDato FROM Bilde WHERE BildeID=%s",
                (bilde_id,)
            )
            # Return user ID, description and uploaded date or None
            result = cursor.fetchone()
            if result:
                return True, result
            else:
                return False, "Image not found."
        except Exception as e:
            return False, f"Database error: {e}"
        finally:
            cursor.close()

    # Add comment
    def add_comment(self, bilde_id, bruker_id, kommentar):
        cursor = self.db.get_cursor()
        try:
            if not self._bilde_exists(cursor, bilde_id):
                return False, "Image Id not found."
            
            if not self._bruker_exists(cursor, bruker_id):
                return False, "User Id not found."
            
            if self._comment_exists(cursor, bilde_id, bruker_id, kommentar):
                return False, "Comment already exists."
            
            cursor.execute(
                "INSERT INTO Kommentar (BildeID, BrukerID, Kommentaren) VALUES (%s, %s, %s)",
                (bilde_id, bruker_id, kommentar)
            )
            self.db.commit()
            return True, "Comment added successfully."
        except Exception as e:
            self.db.rollback()
            return False, f"Error adding comment: {e}"
        finally:
            cursor.close()

    # Get comments by image
    def get_comments_by_image(self, bilde_id):
        cursor = self.db.get_cursor()
        try:
            cursor.execute("SELECT Kommentaren FROM Kommentar WHERE BildeID=%s", (bilde_id,))
            rows = cursor.fetchall()
            if not rows:
                return False, "No comments found."
            return True, [row[0] for row in rows]
        except Exception as e:
            return False, f"Database error: {e}"
        finally:
            cursor.close()

    # Delete comment
    def delete_comment(self, bilde_id, bruker_id, kommentar):
        cursor = self.db.get_cursor()
        try:
            if not self._comment_exists(cursor, bilde_id, bruker_id, kommentar):
                return False, "Comment not found."

            cursor.execute(
                "DELETE FROM Kommentar WHERE BildeID=%s AND BrukerID=%s AND Kommentaren=%s",
                (bilde_id, bruker_id, kommentar,)
            )
            self.db.commit()
            return True, "Comment deleted successfully."
        except Exception as e:
            self.db.rollback()
            return False, f"Error deleting comment: {e}"
        finally:
            cursor.close()

    
    # Get user info by comment
    def get_user_info_by_comment(self, kommentar):
        cursor = self.db.get_cursor()
        try:
            cursor.execute(
                """
                SELECT Bruker.BrukerID, Bruker.Fornavn, Bruker.Etternavn
                FROM Bruker
                JOIN Kommentar ON Bruker.BrukerID = Kommentar.BrukerID
                WHERE Kommentaren=%s
                """,
                (kommentar,)
            )
            result = cursor.fetchall()
            if result:
                return True, result[0]
            else:
                return False, "No user found for this comment."
        except Exception as e:
            return False, f"Database error: {e}"
        finally:
            cursor.close()

     # Get all image (description) for a specific user.
    def get_bilder_by_user(self, bruker_id):
        cursor = self.db.get_cursor()
        try:
            cursor.execute(
                "SELECT Beskrivelse FROM Bilde WHERE Fotograf=%s",
                (bruker_id,)
            )
            rows = cursor.fetchall()
            if not rows:
                return False, "No images found for this user."
            
            return True, [row[0] for row in rows]
        except Exception as e:
            return False, f"Database error:{e}"
        finally:
            cursor.close()

    # Get comments for a specific description
    def get_comments_by_beskrivelse(self, beskrivelse):
        cursor = self.db.get_cursor()
        try:
            cursor.execute(
                """
                SELECT Kommentar.Kommentaren
                FROM Kommentar
                JOIN Bilde ON Kommentar.BildeID = Bilde.BildeID
                WHERE Bilde.Beskrivelse=%s
                """,
                (beskrivelse,)
            )
            rows = cursor.fetchall()
            if not rows:
                return False, "No comments found for this image description."
            return True, [row[0] for row in rows]
        except Exception as e:
            return False, f"Database error: {e}"
        finally:
            cursor.close()

        

    
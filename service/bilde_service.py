from database import Database

class BildeService:
    def __init__(self, db):
        self.db = db

    # Add image
    def add_image(self, bilde_id, beskrivelse, dato, fotograf):
        cursor = self.db.get_cursor()
        try:
            # Check if photographer exists
            cursor.execute(
                "SELECT COUNT(*) FROM Bruker WHERE BrukerID=%s", 
                (fotograf,)
            )
            if cursor.fetchone()[0] == 0:
                return False, "Photographer does not exist"
        
            # Check if bilde_id already exists
            cursor.execute(
                "SELECT COUNT(*) FROM Bilde WHERE BildeID=%s", 
                (bilde_id,)
            )
            if cursor.fetchone()[0] > 0:
                return False, "BildeID already exists"

            # Adding image
            cursor.execute(
                "INSERT INTO Bilde (BildeID, Beskrivelse, OpplastetDato, Fotograf) VALUES (%s, %s, %s, %s)",
                (bilde_id, beskrivelse, dato, fotograf)
            )
            self.db.commit()
            return True, "Image added successfully"
        except Exception as e:
            self.db.rollback()
            return False, f"Error adding image: {e}"
        finally:
            cursor.close()

    # Find image by ID
    def find_image_by_id(self, bilde_id):
        cursor = self.db.get_cursor()
        try:
            cursor.execute(
                "SELECT BildeID, Beskrivelse, OpplastetDato, Fotograf FROM Bilde WHERE BildeID=%s", 
                (bilde_id,)
            )
            result = cursor.fetchone()
            if result:
                return True, result
            else:
                return False, "Image not found."
        except Exception as e:
            return False, f"Database error: {e}"
        finally:
            cursor.close()

    def update_description(self, bilde_id, ny_beskrivelse):
        cursor = self.db.get_cursor()
        try:
            cursor.execute(
                "UPDATE Bilde SET Beskrivelse=%s WHERE BildeID=%s", 
                (ny_beskrivelse, bilde_id)
            )
            if cursor.rowcount == 0:
                self.db.rollback()
                return False, "Image not found."
            self.db.commit()
            return True, "Description updated successfully"
        except Exception as e:
            self.db.rollback()
            return False, f"Error updating description: {e}"
        finally:
            cursor.close()
        
    
    def delete_image(self, bilde_id):
        cursor = self.db.get_cursor()
        try:
            # Delete from tables likes, comments, tagForBilde before deleteing image
            cursor.execute(
                "DELETE FROM Likes WHERE BildeID=%s", 
                (bilde_id,)
            )
            cursor.execute(
                "DELETE FROM Kommentar WHERE BildeID=%s", 
                (bilde_id,)
            )
            cursor.execute(
                "DELETE FROM TagForBilde WHERE BildeID=%s", 
                (bilde_id,)
            )

             # Delete image
            cursor.execute(
                "DELETE FROM Bilde WHERE BildeID=%s", 
                (bilde_id,)
            )
            if cursor.rowcount == 0:
                self.db.rollback()
                return False, f"No image with ID {bilde_id} exists"
            
            self.db.commit()
            return True, "Image deleted successfully"
        except Exception as e:
            self.db.rollback()
            return False, f"Error deleting image: {e}"
        finally:
            cursor.close()
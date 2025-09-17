from database import Database

class TagForImageService:
    def __init__(self, db):
        self.db = db

    def get_image_info(self, bilde_id):
        cursor = self.db.get_cursor()
        try:
            cursor.execute(
                "SELECT BildeID, Beskrivelse, Fotograf FROM Bilde WHERE BildeID=%s",
                (bilde_id,)
            )
            result = cursor.fetchone()
            if result:
                return True, result
            else:
                return False, f"Image with ID {bilde_id} not found"
        except Exception as e:
            return False, f"Database error: {e}"
        finally:
            cursor.close()

    # Check if hashtag already exists
    def _emneknagg_exists(self, cursor, emneknagg_id):
        cursor.execute(
            "SELECT COUNT(*) FROM Emneknagg WHERE EmneknaggID=%s", 
            (emneknagg_id,)
        )
        return cursor.fetchone()[0] > 0

    # Check is tag already exists
    def _tag_exists(self, cursor, bilde_id, emneknagg_id):
        cursor.execute(
            "SELECT COUNT(*) FROM TagForBilde WHERE BildeID=%s AND EmneknaggID=%s",
            (bilde_id, emneknagg_id)
        )
        return cursor.fetchone()[0] > 0

    def add_tag(self, bilde_id, emneknagg_id):
        cursor = self.db.get_cursor()
        try:
            # Check if image already exists
            if not self.get_image_info(bilde_id):
                return False, f"Image with ID {bilde_id} not found"
            
            if not self._emneknagg_exists(cursor, emneknagg_id):
                return False, f"Hashtag with ID {emneknagg_id} not found"
            
            if self._tag_exists(cursor, bilde_id, emneknagg_id):
                return False, "Tag already exists for this image"

            cursor.execute(
                "INSERT INTO TagForBilde (BildeID, EmneknaggID) VALUES (%s,%s)",
                (bilde_id, emneknagg_id)
            )
            self.db.commit()
            return True, "Tag added successfully"
        except Exception as e:
            self.db.rollback()
            return False, f"Error adding tag {e}"
        finally:
            cursor.close()

    def delete_tag(self, bilde_id, emneknagg_id):
        cursor = self.db.get_cursor()
        try:
            if not self._tag_exists(cursor, bilde_id, emneknagg_id):
                return False, "Tag not found for this image"
            
            cursor.execute(
                "DELETE FROM TagForBilde WHERE BildeID=%s AND EmneknaggID=%s",
                (bilde_id, emneknagg_id)
            )
            self.db.commit()
            return True, "Tag deleted successfully"
        except Exception as e:
            self.db.rollback()
            return False, f"Error deleting tag: {e}"
        finally:
            cursor.close()
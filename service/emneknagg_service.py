from database import Database

class EmneknaggService:
    def __init__(self, db):
        self.db = db

    # Check if hashtag exists
    def _emneknagg_exists(self, cursor, emneknagg_id):
        cursor.execute("SELECT COUNT(*) FROM Emneknagg WHERE EmneknaggID=%s", (emneknagg_id,))
        return cursor.fetchone()[0] > 0

    # Add new hashtag
    def add_emneknagg(self, emneknagg_id, emneknaggen):
        cursor = self.db.get_cursor()
        try:
            if not emneknagg_id or not emneknaggen:
                return False, "Both ID and tag are required."
            
            if self._emneknagg_exists(cursor, emneknagg_id):
                return False, f"Hashtag with ID {emneknagg_id} already exists."
            
            cursor.execute(
                "INSERT INTO Emneknagg (EmneknaggID, Emneknaggen) VALUES (%s, %s)",
                (emneknagg_id, emneknaggen)
            )
            self.db.commit()
            return True, "Hashtag added succesfully."
        except Exception as e:
            self.db.rollback()
            return False, f"Database error: {e}"
        finally:
            cursor.close()

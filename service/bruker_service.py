from database import Database

class UserService:
    def __init__(self, db):
        self.db = db

    def get_user(self, bruker_id):
        try:
            cursor = self.db.get_cursor()
            cursor.execute(
                "SELECT BrukerID, Fornavn, Etternavn, Epost FROM Bruker WHERE BrukerID=%s", 
                (bruker_id,)
            )
            result = cursor.fetchone()
            cursor.close()
            if result:
                return True, result
            else:
                return False, "User not found."
        except Exception as e:
            return False, f"Database error: {e}"

    def add_user(self, bruker_id, fornavn, etternavn, epost):
        try:
            exists, result = self.get_user(bruker_id)
            if exists:
                return False, "User ID already exists."
            
            cursor = self.db.get_cursor()
            cursor.execute(
                "INSERT INTO Bruker (BrukerID, Fornavn, Etternavn, Epost) VALUES (%s, %s, %s, %s)",
                (bruker_id, fornavn, etternavn, epost)
            )
            self.db.commit()
            cursor.close()
            return True, "User added successfully."
        except Exception as e:
            return False, f"Database error: {e}"

    def update_email(self, bruker_id, ny_epost):
        try:
            cursor = self.db.get_cursor()
            cursor.execute(
                "UPDATE Bruker SET Epost=%s WHERE BrukerID=%s", 
                (ny_epost, bruker_id)
            )
            if cursor.rowcount == 0:
                cursor.close()
                return False, "User not found."
            self.db.commit()
            cursor.close()
            return True, "Email updated sucessfully."
        except Exception as e:
            return False, f"Database error: {e}"
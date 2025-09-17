import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="Bildesjef",
            password="oblig2024",
            database="oblig2024"
        )

    # Method to run a query
    def get_cursor(self):
        return self.connection.cursor()
    
    # Method to commit changes
    def commit(self):
        self.connection.commit()

    # Method to close the connection
    def close(self):
        self.connection.close()

    # Method for rollback
    def rollback(self):
        self.connection.rollback()
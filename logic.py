import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def get_car_img(self, car_id):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT image FROM cars WHERE car_id = ?", (car_id, ))
            result = cur.fetchall()
            return result[0][0]
    def get_car_name(self, car_id):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT car_name FROM cars WHERE car_id = ?", (car_id, ))
            result = cur.fetchall()
            return result[0][0]
                
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
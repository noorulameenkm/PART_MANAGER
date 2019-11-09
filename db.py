import sqlite3

class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.connection.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM parts")
        rows = self.cursor.fetchall()
        return rows

    def add_part(self, part, customer, retailer, price):
        self.cursor.execute("INSERT INTO parts values(NULL, ?, ?, ?, ?)", (part, customer, retailer, price))
        self.connection.commit()

    def remove_part(self, id):
        self.cursor.execute("DELETE FROM parts where id = ?", (id,))
        self.connection.commit()

    def update_part(self, id, part, customer, retailer, price):
        self.cursor.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ? ", (part, customer, retailer, price, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()

# db = Database('store.db')

# db.add_part("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
# db.add_part("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.add_part("500w PSU", "Karen Johnson", "Newegg", "80")
# db.add_part("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.add_part("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.add_part("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.add_part("600w Corsair PSU", "Karen Johnson", "Newegg", "130")

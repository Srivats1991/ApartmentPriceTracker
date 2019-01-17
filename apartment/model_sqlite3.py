"""
Simple recipesbook flask app
"""
from .Model import Model
import sqlite3
#file for the database
DB_FILE = 'entries.db'

class model(Model):
    def __init__(self):
    	"""
    	Makes sure the connection to database is completed.
    	"""
    	connection = sqlite3.connect(DB_FILE)
    	cursor = connection.cursor()
    	try:
    		cursor.execute("select count(rowid) from apartments")
    	except sqlite3.OperationalError:
    		cursor.execute("create table apartments (Address, Phone no, Beds, Price Range , Title, zipcode)")
    	cursor.close()

    def select(self):
        """
        Fetches all rows from the database
        Each row contains: title,author,ingredients,timetaken,skillset,description
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM apartments")
        return cursor.fetchall()

    def insert(self, address, phone, beds, price, title, zipcode):
        """
        Inserts entry into database
        :param Address: String
        :param author: String
        :param ingredients: String
        :param timetaken: String
        :param skillset: String
        :param description: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'address':address, 'phone':phone, 'beds':beds, 'price':price, 'title':title, 'zipcode':zipcode}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into apartments (address, phone, beds, price, title, zipcode) VALUES (:address, :phone, :beds, :price, :title, :zipcode)", params)

        connection.commit()
        cursor.close()
        return True
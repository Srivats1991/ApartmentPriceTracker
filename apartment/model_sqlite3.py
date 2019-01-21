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
            cursor.execute("select * from apartments")
            print("My dear...Table already exists...")
        except sqlite3.OperationalError:
            print("Creating a new table apartments that doesn't exist....")
            cursor.execute("create table apartments (city, state, address, phone, beds, price , title)")
        cursor.close()

    def select(self,city,state):
        """
        Fetches all rows from the database
        Each row contains: title,author,ingredients,timetaken,skillset,description
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT address, phone, beds, price, title FROM apartments where city = '{0}' and state = '{1}' ;".format(city, state))
        return cursor.fetchall()

    def insert(self, city, state, address, phone, beds, price, title):
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
        params = {'city':city, 'state':state, 'address':address, 'phone':phone, 'beds':beds, 'price':price, 'title':title}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into apartments (city, state, address, phone, beds, price, title) VALUES (:city, :state, :address, :phone, :beds, :price, :title)", params)

        connection.commit()
        cursor.close()
        return True
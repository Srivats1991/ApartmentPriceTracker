"""
Base class for recipe model
"""
class Model():
    def select(self):
        """
        This function returns all the records in the recipe model.
        :return: python list containing all the elements. 
        """
        pass

    def insert(self, address, phone, beds, price, title, zipcode):
        """
        Inserts entry into the database
        :param title: String
        :param author: String
        :param ingredients: String
        :param timetaken: String
        :param skillset: String
        :param description: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
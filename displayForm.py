"""
displayForm presenter via MethodView
"""
from flask import render_template
from flask.views import MethodView
import apartment

class DisplayForm(MethodView):
	def get(self):
		"""This function gets all the entries of the recipe model. It uses HTTP GET via get() method.
		:return: it passes the dictionary to displayForm.html Jinja2 template using render_template.
		"""
		model = apartment.get_model()
		elements = []
		entries = [dict(address=elements[0],phone=elements[1],beds=elements[2],price=elements[3],title=elements[4], zipcode=elements[5]) for elements in model.select()]

		return render_template('displayForm.html', entries=entries)

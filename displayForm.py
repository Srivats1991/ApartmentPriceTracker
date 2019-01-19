"""
displayForm presenter via MethodView
"""
from flask import render_template
from flask.views import MethodView
import apartment

class DisplayForm(MethodView):
    def get(self, city, state):
        """This function gets all the entries of the recipe model. It uses HTTP GET via get() method.
        :return: it passes the dictionary to displayForm.html Jinja2 template using render_template.
        """
        model = apartment.get_model()
        # city = request.args.get['city']
        # state = request.args.get['state']
        city = city
        state = state

        elements = []
        entries = [dict(address=elements[0],phone=elements[1],beds=elements[2],price=elements[3],title=elements[4]) for elements in model.select(city, state)]
        print(entries[0])
        return render_template('displayForm.html', entries=entries)

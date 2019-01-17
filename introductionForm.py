"""
Introduction form presenter via MethodView
"""
from flask import render_template
from flask.views import MethodView
import apartment

class IntroductionForm(MethodView):
    def get(self):
        """This function renders the landing page with introduction.
        :return: the landing page in introductionForm.html is rendered on Jinja2 template using render_template"""
        return render_template('introductionForm.html')
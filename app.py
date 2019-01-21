"""
A scalable flask model app for recipes.
"""
import flask
from flask.views import MethodView
from introductionForm import IntroductionForm
from displayForm import DisplayForm
from insertForm import InsertForm
from crawlForm import CrawlForm

#creates app as a flask object
app = flask.Flask(__name__)

#default landing page using route() method of flask for recipe model
#app.add_url_rule('/',view_func=InsertForm.as_view('insertForm'),methods=['GET','POST'])

app.add_url_rule('/',view_func=IntroductionForm.as_view('introductionForm'),methods=['GET'])
app.add_url_rule('/insert', view_func=InsertForm.as_view('insertForm'),methods=['GET','POST'])

app.add_url_rule('/crawl', view_func=CrawlForm.as_view('crawlForm'), methods=['GET','POST'])
#display recipes page using route() method of flask for recipe model
app.add_url_rule('/display/?city=<city>&state=<state>',view_func=DisplayForm.as_view('displayForm'),methods=['GET'])


#using run() method of flask, launch the web app on all IP addresses of the host using port 8000 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
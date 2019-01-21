"""
insertForm presenter via MethodView
"""
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import apartment
import requests
from bs4 import BeautifulSoup
import pandas

class InsertForm(MethodView):
    def get(self):
        """This function renders the insert form.
        :return: the insert form in insertForm.html is rendered on Jinja2 template using render_template
        """
        return render_template('insertForm.html')

    def post(self):
        """
        Accepts POST requests, and processes the form.
        Redirects to introduction form when completed.
        """
        model = apartment.get_model()
        city = request.form['city']
        state = request.form['state']

       #  base_url = "https://www.apartments.com/{0}-{1}/1-bedrooms-1-bathrooms/".format(city,state)
       #  print(base_url)
       #  # base_url = 'https://www.apartments.com/portland-or/1-bedrooms-1-bathrooms/'
       # # city = base_url[24:-27].replace('/','-')
       #  # To get the html contents
       #  headers = requests.utils.default_headers()
       #  headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

       #  r = requests.get(base_url, headers=headers)
       #  c = r.content

       #  # To parse the html
       #  soup = BeautifulSoup(c,"html.parser")

       #  # To extract the first and last page numbers
       #  paging = soup.find("div",{"id":"placardContainer"}).find("div",{"id":"paging"}).find_all("a")
       #  #print ("\n this is the number of pages we got {0} ..\n ".format(paging))
       #  start_page = paging[1].text
       #  last_page = paging[len(paging)-2].text
       #  web_content_list = []

       #  for page_number in range(int(start_page),int(last_page) + 1):
    
       #      # To form the url based on page numbers
       #      # url = base_url+str(page_number)+"/.html"
       #      # print('\n Requesting  {0}  url'.format(base_url + str(page_number) + "/"))
       #      r = requests.get(base_url+str(page_number)+"/", headers=headers)
       #      # print('\n this is the request url {0}'.format(r))
       #      c = r.content
       #      soup = BeautifulSoup(c,"html.parser")

       #      # To extract the Title and the Location
       #      placard_header = soup.find_all("header",{"class":"placardHeader"})

       #      # print ("\n this is the placardHeader {0} \n".format(placard_header))
            
       #      # To extract the Rent, No of Beds and Phone Number
       #      placard_content = soup.find_all("section",{"class" :"placardContent"})

       #      # print ("\n this is the placardContent {0} \n".format(placard_content))
            
       #      # To process property by property by looping
       #      for item_header,item_content in zip(placard_header,placard_content):
       #        # To store the information to a dictionary
       #          web_content_dict = {}
       #          try:
       #              web_content_dict["title"]=item_header.find("a",{"class":"placardTitle js-placardTitle"}).text
       #          except:
       #              print("it's dead jim {0}".format(item_header))
       #              web_content_dict["title"] = ''
       #              pass
       #          web_content_dict["address"] = item_header.find("div",{"class":"location"}).text
       #          web_content_dict["price"] = item_content.find("span",{"class":"altRentDisplay"}).text
       #          web_content_dict["beds"] = item_content.find("span",{"class":"unitLabel"}).text
       #          web_content_dict["phone"] = item_content.find("div",{"class":"phone"}).find("span").text
       #          web_content_dict["city"] = city
       #          web_content_dict["state"] = state
       #          print("This is the entry being inserted {0}".format(web_content_dict))
       #          # To store the dictionary to into a list
       #        #  web_content_list.append(web_content_dict)
       #          model.insert(web_content_dict['city'], web_content_dict['state'], web_content_dict['address'], web_content_dict['phone'], web_content_dict['beds'], web_content_dict['price'], web_content_dict['title'])
        # To make a dataframe with the list
      #  df = pandas.DataFrame(web_content_list)
      #  print(elements for elements in web_content_list)
        # To write the dataframe to a csv file
      #  df.to_csv("Output_{0}.csv".format(city))

       
        return redirect(url_for('displayForm',city=city, state=state))
        

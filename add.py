import jinja2
import os
import webapp2
from google.appengine.ext import ndb
import datetime
import logging

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AddPet(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/addpet.html')
        self.response.out.write(template.render())
    def post(self):
        petname = self.request.get("petname")
        atype = self.request.get("type")
        breed = self.request.get("breed")
        description = self.request.get("description")
        date = self.request.get('time_posted')
        age = int(self.request.get("age"))
        # add image url here

        new_pet(petname, atype, breed, description, age, date,) #add image argument
        self.response.out.write("You have submitted your pet <br>")
        self.response.out.write("<a href='/addpet'> add another pet</a>") #sketch way of adding html thru python
        # self.redirect('/')


class AddPet2DS(ndb.Model):
    petname = ndb.StringProperty()
    atype = ndb.StringProperty()
    breed = ndb.StringProperty()
    time_posted = ndb.DateProperty()
    description = ndb.StringProperty()
    age = ndb.IntegerProperty()
    # add image here


def new_pet(petname, atype, breed, description, age, time_posted): #add image argument
  """Puts a new pet into Datastore."""
  newpet = AddPet2DS(petname=petname, age=age, atype=atype, time_posted=datetime.datetime.now(), breed=breed, description = description)
  return newpet.put()

logging.info(AddPet2DS.query().get())
print AddPet2DS.query().get()

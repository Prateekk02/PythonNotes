import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__),'..')))   # Joins the path of all the files


from payment import payment_details

def course():
    print("This is my course details")

course()
payment_details.payment()
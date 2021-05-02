# code en python, inshallah

import tweepy 
import json
import random 
import credentials # fichier pour se connecter à l'app

api,auth = credentials.auth()
api.update_status(status="hello world")





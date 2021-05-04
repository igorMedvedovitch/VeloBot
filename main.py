# code en python, inshallah

import tweepy 
import json
import random 
import auth
# fichier pour se connecteri a l'app

api,auth = auth.auth("credentials")
api.update_status(status="hello world")





import tweepy
import json

# creer un fichier credential de la forme : 
#
#{
#    "api_key" : "xxxxxxxx", 
#    "api_secret_key" : "xxxxxxxxxxxe",	
#    "access_token" : "xxxxxxxxxxxxxxxx",
#    "access_token_secret" : "xxxxxxxxxxxxxxxxxx"
#}
#


def auth(credentialjason):
   #ouvre le json avec les crédits. 
   credentials = json.loads(open(credentialjason).read())
   # Clés de votre application
   consumer_key = credentials["api_key"] 
   consumer_secret = credentials["api_secret_key"]	

   # le access_token est le token de l'application twitter que nous avons créée précédement
   access_token = credentials["access_token"]
   access_token_secret = credentials["access_token_secret"]

   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(access_token, access_token_secret)

   api = tweepy.API(auth)
   return api,auth


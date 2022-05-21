from django.shortcuts import render
from django.http import HttpResponse

import tweepy
import os
 
# Consumer keys and access tokens, used for OAuth
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')
bearer_token = os.environ.get('bearer_token')

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def postCuacaTwt(request):
    if request.method != "POST" :
        return HttpResponse("wrong method")

    api.update_status_with_media(status=request.POST["description"], filename="foto", file=request.FILES["image"])
    return HttpResponse("Successfully post to twitter")
from django.shortcuts import render
from django.http import HttpResponse
import feedparser

from dict_hash import dict_hash


def index(request):

    if request.GET.get("url"):
        url = request.GET["url"] #Getting URL
        feed = feedparser.parse(url) #Parsing XML data
        pass

        for e in feed['entries']:
            e['hash'] = dict_hash(e)
        
        pass

    else:
        feed = None

    return render(request, 'rss/reader.html', { 'feed' : feed, })


def sort_asc(request):

    if request.GET.get("url"):
        url = request.GET["url"] #Getting URL
        feed = feedparser.parse(url) #Parsing XML data

        # TODO: feed sa musi nasortovat podla datumu od najstarsieho

    else:
        feed = None

    return render(request, 'rss/reader.html', { 'feed' : feed, })
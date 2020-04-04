from django.shortcuts import render
from django.http import HttpResponse

import feedparser
from operator import itemgetter


def index(request):

    if request.GET.get("url"):
        url = request.GET["url"] #Getting URL
        feed = feedparser.parse(url) #Parsing XML data

        request.session['url'] = url

        for e in feed['entries']:
            e['hash'] = 'p-' + str(abs(hash(e['title'])) % (10 ** 8))
        
        pass

    else:
        feed = None

    return render(request, 'rss/reader.html', { 'feed' : feed, })


def sort_a(request):

    url = request.session['url']
    feed = feedparser.parse(url)

    entries = feed['entries']
    entries_asc_sorted = sorted(entries, key=itemgetter('published_parsed'))

    for e in entries_asc_sorted:
        e['hash'] = 'p-' + str(abs(hash(e['title'])) % (10 ** 8))
        
    feed['entries'] = entries_asc_sorted

    return render(request, 'rss/reader.html', { 'feed' : feed, })


def sort_d(request):

    url = request.session['url']
    feed = feedparser.parse(url)

    entries = feed['entries']
    entries_asc_sorted = sorted(entries, key=itemgetter('published_parsed'), reverse=True)

    for e in entries_asc_sorted:
        e['hash'] = 'p-' + str(abs(hash(e['title'])) % (10 ** 8))
        
    feed['entries'] = entries_asc_sorted

    return render(request, 'rss/reader.html', { 'feed' : feed, })
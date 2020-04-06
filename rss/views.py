from django.shortcuts import render
from django.http import HttpResponse

import feedparser
from operator import itemgetter
import html
    

def hash_entries(feed):
    for e in feed['entries']:
            e['hash'] = 'p-' + str(abs(hash(e['title'])) % (10 ** 8))
            e['summary'] = html.unescape(e['summary'])     # unescape html symbols
    
    return feed


def sort_entries(feed, sort):
    entries = feed['entries']
    
    if sort == 'ASC':
        sorted_entries = sorted(entries, key=itemgetter('published_parsed'))
    elif sort == 'DESC':
        sorted_entries = sorted(entries, key=itemgetter('published_parsed'), reverse=True)
    else:
        sorted_entries = entries  # no sorting

    feed['entries'] = sorted_entries
    return feed


def prepare_feed(feed, sort=None):
    feed_with_hashed_entries = hash_entries(feed)
    feed_with_sorted_entries = sort_entries(feed_with_hashed_entries, sort)
    return feed_with_sorted_entries


def index(request):

    if request.GET.get("url"):
        url = request.GET["url"]
        feed = feedparser.parse(url)

        request.session['url'] = url

        feed = prepare_feed(feed, sort=None)        
        sort_enable = True

    else:
        feed = None
        sort_enable = False

    return render(request, 'rss/reader.html', { 'feed' : feed, 'sort_enable' : sort_enable, })


def sort_articles_ascending(request):   # oldest article first

    url = request.session['url']
    feed = feedparser.parse(url)

    feed = prepare_feed(feed, sort='ASC')

    return render(request, 'rss/reader.html', { 'feed' : feed, 'sort_enable' : True, })


def sort_articles_descending(request):  # newest article first

    url = request.session['url']
    feed = feedparser.parse(url)

    feed = prepare_feed(feed, sort='DESC')

    return render(request, 'rss/reader.html', { 'feed' : feed, 'sort_enable' : True, })
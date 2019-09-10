from django.http import HttpResponse
from django.shortcuts import render
import operator
# Create your views here.

def index(request):
  return render(request, 'index.html',)

def count(request):
  fulltext = request.GET['fulltext']
  wlist = fulltext.split()
  d = {}

  for w in wlist:

    if w in d:
      d[w] += 1
    else:
      d[w] = 1

  sortedwords = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

  context = {
    'fulltext'   : fulltext,
    'count'      : len(wlist),
    'sortedwords': sortedwords
  }
  return render(request, 'count.html', context)
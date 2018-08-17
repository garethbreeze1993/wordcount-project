from django.http import HttpResponse
import datetime
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'wordcount/home.html')
	
def current_time(request):
    now = datetime.datetime.now()
    return HttpResponse('<h2>The current time is {}</h2>'.format(now))

def count(request):
    fulltext = request.GET['fulltext'] # this gets what we typed in in our word count box. Because it adds what we typed on to the count url
    wordlist = fulltext.split()
    worddictionary = {}
# the for loop counts words in the text if it is a new word it adds it to the dictionary as a key, the value to this is an integer 
#if it is already there it adds 1 to the value for the word.
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+= 1		
        
        else:
            worddictionary[word]=1	

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True) 
	# basicaly looks at value for the key, the reverse means what order you want it to happen to.			
        	
    return render(request, 'wordcount/count.html', {'fulltext':fulltext,'wordcount':len(wordlist),'sortedwords':sortedwords})

#worddictionary.items() turns the dictionary into a list which will have two things to work with
# thus needing to put two things in for loop.

def about(request):
    return render(request, 'wordcount/about.html')	
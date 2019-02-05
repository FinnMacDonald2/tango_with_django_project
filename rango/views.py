from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
        # Construct a dictionary to pass to the template engine as its context.
        # Note the key boldmessage is the same as {{ boldmessage }} in the template
        context_dict = {'boldmessage': "Sub 2 WillNE"}

        #This returns a rendered response to send to the client.
        #Makes use of the shortcut function to make our lives easier.
        #First parameter is always the template we wish to use.

        return render(request, 'rango/index.html', context=context_dict)
        

def about(request):

        context_dict = {}

        return render(request, 'rango/about.html', context=context_dict)


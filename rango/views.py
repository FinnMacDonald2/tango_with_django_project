from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rango.models import Category, Page


def index(request):
        # Query the database for a list of ALL categories currently stored.
        # Order the categories by no. likes in descending order.
        # Retrieve the top 5 only - or all if less than 5.
        # Place the list in our context_dict dictionary
        # that will be passed to the template engine.

        
        category_list = Category.objects.order_by('-likes')[:5]
        page_list = Page.objects.order_by('-views')[:5]
        context_dict = {'categories': category_list, 'pages':page_list}

        #This returns a rendered response to send to the client.
        #Makes use of the shortcut function to make our lives easier.
        #First parameter is always the template we wish to use.

        return render(request, 'rango/index.html', context=context_dict)
        

def about(request):

        context_dict = {}

        return render(request, 'rango/about.html', context=context_dict)



def show_category(request, category_name_slug):

        #Context_dict to pass to the template renderer masheen

        context_dict = {}

        try:
                #Look for a slug with the given name
                #Cant find one, then .get() raises an exception

                category = Category.objects.get(slug=category_name_slug)


                #Retrive list of associated pages

                pages = Page.objects.filter(category=category)

                # Adds our results list to the template context under name pages

                context_dict['pages'] = pages
                #We also add the category object from the database to verify that it exists

                context_dict['category'] = category
        except Category.DoesNotExist:
                #oopsie whoopsie uwu
                context_dict['category'] = None
                context_dict['pages'] = None
        return render(request, 'rango/category.html', context_dict)

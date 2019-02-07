import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')


import django
django.setup()
from rango.models import Category, Page

def populate():
    #Create lists of dictionaries containing the pages for each category
    ## Then we will create a dictionary of dictionaries for our categories.
    #This lets us iterate through each data strucutre

    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/",
         "views": 5},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/",
         "views": 3},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/",
         "views": 2}]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 3},
        {"title":"Django Rocks", "url":"http://www.djangorocks.com/",
         "views": 8},
        {"title":"How to Tango with Django", "url":"http://www.tangowithdjango.com/",
         "views": 100}]
    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/",
         "views": 2},
        {"title":"Flask",
         "url":"htpp://flask.pocoo.org",
         "views": 1}]

    cats = {"Python": {"pages" : python_pages, "views":128, "likes":64},
            "Django": {"pages" : django_pages, "views":64, "likes":32 },
            "Other Frameworks": {"pages": other_pages,"views":32, "likes":16}}

    #To add more categories or pages, just add them to the dictionaries above

    #Code below goes thorugh the cats dictionary, then adds all the associated pages for that category


    for cat, cat_data in cats.items():
        c = add_cat(cat, cats[cat]["views"],cats[cat]["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

        #prints the categories we have added
        for c in Category.objects.all():
            for p in Page.objects.filter(category=c):
                print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    c.save()
    return c


# Start execution here!

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()

    

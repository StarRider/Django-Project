from django.shortcuts import render
from .models import Post

page = 0

with open("content.txt","r") as f:
    material = f.read()
    
posts = { 'author': 'Sharon',
           'title': 'I am what I am.',
           'media':'https://www.youtube.com/embed/cBxOZqtGTXE',
           'content': material,
           'datePosted':'March 23rd, 2019'
        }

# -- supplementory functions    
def base(request):
    global page
    post = Post.objects.all()[page]
    context = {
            'post':post,
            'title': 'WhiteFlames-Home',
            'postNum':page
    }
    return render(request, 'WhiteFlames/home.html', context)
# -- supplementory functions

def home(request):
    # for home button
    global page
    page = 0
    return base(request)

def nextPage(request):
    # for next button
    global page
    if page + 1 < len(Post.objects.all()):
        page += 1
    else:
        page = 0
    return base(request)
    
def prevPage(request):
    # for next button
    global page
    if page - 1 >= 0:
        page -= 1
    else:
        page = len(Post.objects.all()) - 1
    return base(request)


def about(request):
    # for about button
    context = {
            'title':'WhiteFlames-About' ,
            'aboutTitle': 'Who are we?',
            'aboutContent': "OYO Rooms, commonly known as OYO, is India's largest hospitality company, consisting mainly of budget hotels. It was founded in 2013 by Ritesh Agarwal and has since grown to over 8,500 hotels in 337 cities in India, Malaysia, UAE, Nepal, China and Indonesia."
    }
    return render(request, 'WhiteFlames/about.html', context)
    

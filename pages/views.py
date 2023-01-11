from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.

def page(request, pagename):
    print(pagename)
    pages = get_object_or_404(Page, permalink=pagename)

    return render(request, 'pages/page.html', {'page':pages})

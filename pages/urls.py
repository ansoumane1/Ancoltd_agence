from django.urls import path 
from . import views

urlpatterns = [
    path('<slug:pagename>', views.page, name='page' )
]
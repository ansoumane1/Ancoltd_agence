
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('myapp.urls')),
    path('pages/', include('pages.urls')),
    path('MassogbeAdmin/', admin.site.urls),

]

#handler404 = 'pages.views.handle404'
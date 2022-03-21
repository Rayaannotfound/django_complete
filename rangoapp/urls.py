from django.urls import path
from rangoapp import view
from django.conf import settings
from django.conf.urls.static import static


app_name = 'rangoapp'
urlpatterns = [
    path('', view.index, name='index'),
    path('about/', view.about, name='about'),
]

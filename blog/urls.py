from django.urls import path
#The next line imports all the views from the current directory, which is blog.
from . import views

#We create a url pattern using the path function we imported from django. 
#The first argument is empty cause we want the base URL to return that view. AKA the URL as is, like the landing page
#The 2nd arg tells django to display the view called post_list
#The last arg gives the name post_list to the URL. We want to name each URL.
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
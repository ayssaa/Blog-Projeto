from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup),
    # Login
    path('login', views.login_user),
    
    path('home/', views.home),
    path('newpost', views.newPost),
    path('post/<int:pk>/newcomment', views.newcomment),
    path('mypost', views.myPost),
    path('signout', views.signout),
    path('post/<int:pk>/', views.post_details, name='post_details')

]

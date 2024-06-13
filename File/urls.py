from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
    # path('admin-page/', views.admin_page, name='admin-page'),
    path('search/', views.search, name='search'),
    path('mylist/', views.mylist, name='mylist'),
]

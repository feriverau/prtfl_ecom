from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('search',views.search,name='search'),
    path('category/<slug:slug>',views.category,name='category'),
    path('<slug:slug>',views.detail,name='detail'),
] 
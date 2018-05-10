from django.urls import path
from .import views

app_name='blog'
urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('<slug:slug>',views.post,name='post'),
    path('contato/',views.contato,name='contato'),

]
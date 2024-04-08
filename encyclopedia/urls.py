from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<str:title>', views.entry, name="entry"),
    path("wiki/<str:title>", views.entry,name="entry"),
    path('search/',views.search,name='search'),
    path('newpage/',views.newpage,name='newpage'),
    path('edit/',views.edit,name= 'edit'),
    path('save_edit/',views.save_edit,name= 'save_edit'), 
    path('random_page/',views.random_page,name= "random_page"),
]

from django.urls import path
from . import views

#register the app namespace
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name = 'example'),
    path('variable/', views.variable, name = 'variable'),
    path('inherit/', views.inherit, name = 'inherit')
]
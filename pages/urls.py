from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('apply/', views.apply, name='apply'),
    path('wait/', views.wait, name='wait'),
    path('admission/', views.admission, name='admission'),
]

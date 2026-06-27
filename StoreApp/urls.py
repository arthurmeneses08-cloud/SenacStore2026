from django.urls import include, path
from StoreApp import views  

urlpatterns = [
    path('', views.index, name='home'),
    path('produtos/', views.produtos, name='produtos')
]

"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
     #item category url
    path('item/category/', ItemCategoryCrud.as_view(), name='category_list_create'),
    path('item/category/<int:pk>/', ItemCategoryCrud.as_view(), name='category_detail'),

    
    #item form url
    path('item/form/', ItemFormCrud.as_view(), name='form_list_create'),
    path('item/form/<int:pk>/', ItemFormCrud.as_view(), name='form_detail'),

    
    #item manufacturer url
    path('item/manufacturer/', ItemManufacturerCrud.as_view(), name='manufacturer_detail'),
    path('item/manufacturer/<int:pk>/', ItemManufacturerCrud.as_view(), name='manufacturer_detail'),
    
    #item unit url
    path('item/unit/', ItemUnitCrud.as_view(), name='unit_detail'),
    path('item/unit/<int:pk>/', ItemUnitCrud.as_view(), name='unit_detail'),
    

    # GET by ID, PUT, PATCH, DELETE
   

]

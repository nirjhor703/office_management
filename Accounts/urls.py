from django.urls import path
from .views import *

urlpatterns = [
    #transaction main  urls
    path('transactions/main/', TransactionMainCrud.as_view(), name='transaction_list_create'),
    path('transactions/main/<int:pk>/', TransactionMainCrud.as_view(), name='transaction_main'),

    #transaction head urls
    path('transactions/head/', TransactionHeadCrud.as_view(), name='transaction_list_create'),
    path('transactions/head/<int:pk>/', TransactionHeadCrud.as_view(), name='transaction_head'),

    #transaction head urls
    path('transactions/groupe/', TransactionGroupeCrud.as_view(), name='transaction_list_create'),
    path('transactions/groupe/<int:pk>/', TransactionGroupeCrud.as_view(), name='transaction_groupe'),
]

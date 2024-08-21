from django.urls import path
from .views import index,delete_transaction
urlpatterns = [
    
    path('',index,name="index"),
    path('/delete/<pk>',delete_transaction,name="delete_transaction"),
]
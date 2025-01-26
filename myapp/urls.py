from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home,name='home'),
    path('delete<int:id>/',remove_data,name='deletedata'),
    path('<int:id>/',update_data,name='updatedata')

]

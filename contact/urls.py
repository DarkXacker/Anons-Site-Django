from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='contact'),
    path('contact_list', Contact_list.as_view(), name='contact_list'),

]
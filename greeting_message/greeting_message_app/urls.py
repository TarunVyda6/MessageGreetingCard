from django.urls import path
from . import views

urlpatterns = [

    path('', views.greeting, name='greeting'),
    path('get_card_data/', views.GreetingView.as_view())

]

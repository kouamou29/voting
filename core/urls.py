from django.urls import path


from . import views



urlpatterns = [
    path('',  views.index, name='index'),
    path('register/',  views.register, name='register'),
    #path('vote/<str:pk>/',  views.mility, name='mility'),
    #path('detail_mility/<str:pk>/',  views.detail_mility, name='detail_mility'),
    path('formmility/',  views.formmility, name='formmility'),
]
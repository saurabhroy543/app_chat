from django.urls import path
from .views import index, login, signup, chatPage, logout_view

urlpatterns = [
    path('dashboard', index),
    path('login',login),
    path('signup',signup),
    path("", chatPage, name="chat-page"),
    path('logout/', logout_view, name='logout'),
]

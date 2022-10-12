from django.contrib.auth.views import logout
from django.urls import path
from chat.views import *
from . import views
from ChatApp.settings import *


urlpatterns = [

    path('', inicio, name='inicio'),
    path('index', views.index, name='index'),
    path('chat/', views.chat_view, name='chats'),
    path('padre/', views.padre_view, name='padre'),
    path('nosotros/', nosotros, name='nosotros'),
    path('register/', views.register_view, name='register'),
    path('logout/', logout, {'next_page': 'inicio'}, name='logout'),
    path('form_blog/', form_blog, name= 'form_blog'),
    path("buscarblog/", buscarblog, name="buscarblog"),

    #apartado del chat

    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
]




from django.contrib.auth.views import LogoutView
from django.urls import path
from chat.views import *
from ChatApp.settings import *

urlpatterns = [
        #nombre                 view                    url
    path('',                    inicio,             name='inicio'),
    path('nosotros/',           nosotros,           name='nosotros'),
    path("resultadosblog/",     resultadosblog,     name='resultadosblog'),
    path('form-blog/',          form_blog,          name='form_blog'),
    path('chat',                chat_view,          name='chats'),
    path('padre/',              padre_view,         name='padre'),

#Apartado de Blogs

    path('blog-del/<id>/',             blog_del,         name='blog_del'),
    path('blog-edit/<id>/',            blog_edit,        name='blog_edit'),
    path('blog-view/<id>/',            blog_view,        name='blog_view'),

#Apartado del Usuario
    path('user/',                   user,               name='user'),
    path('index',                   index,              name='index'),
    path('register',                register_view,      name='register'),
    path('MenuBlogs/',         user_MenuBlogs,     name='user_MenuBlogs'),
    path("Edit/",              user_Edit,          name="user_Edit"),
    path('EditPass/',          user_EditPass,      name='user_EditPass'),
    path('AddAvatar/',         user_AddAvatar,     name='user_AddAvatar'),
    path('MisBlogs/',          user_MisBlogs,      name='user_MisBlogs'),

#Apartado del ChatApp
    path('chat/<int:sender>/<int:receiver>',          message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>',  message_list, name='message-detail'),
    path('api/messages',                              message_list, name='message-list'),

#Logout
    path('logout/',  LogoutView.as_view(template_name='chat/logout.html'), name='logout'),
]

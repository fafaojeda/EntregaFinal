from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import *
from chat.forms import *
from chat.serializers import MessageSerializer

#Views posibles para Invitado
def padre_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, 'chat/padre.html',
            {'users': User.objects.exclude(username=request.user.username) })

def inicio(request):
    if request.user.is_authenticated:
        return render(request, "chat/inicio.html" ,{'avatar':obteneravatar(request)})
    else:
        return render(request, "chat/inicio.html")

def nosotros(request):
    if request.user.is_authenticated:
        return render(request, "chat/nosotros.html",{'avatar':obteneravatar(request)})
    else:
        return render(request, "chat/nosotros.html")

def resultadosblog(request):
    Blogs=Blog.objects.all()
    if request.user.is_authenticated:
        return render(request, "chat/resultadosblog.html",{'Blog':Blogs ,'avatar':obteneravatar(request)})
    else:
        return render(request, "chat/resultadosblog.html",{'Blog':Blogs})

#Apartado de Blogs
@login_required
def blog_del(request,id):
    blog=Blog.objects.get(id,id)
    blog.delete()
    return redirect(to='user_MisBlogs.html')

#Registro
def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            email    = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password, email=email)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('inicio')
    else:
        form = SignUpForm()
        template = 'chat/register.html'
        context = {'form':form}
        return render(request, template, context)

#Login
def index(request):
    if request.user.is_authenticated:
        return redirect('padre')
    if request.method == 'GET':
        return render(request, 'chat/index.html')
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse('{"error": "User does not exist"}')
        return redirect('inicio')

#Apartado del Usuario
@login_required
def user_AddAvatar(request):
    if request.method=='POST':
        formulario          =AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo     = Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo[0].delete()
            avatar          =Avatar (   user=request.user, 
                                        imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'chat/inicio.html', {'usuario':request.user, 'mensaje':'Avatar Agregado Exitosamente', "avatar": avatar.imagen.url})
        else:
            return render(request, 'chat/user_AddAvatar.html', {'formulario':formulario, 'mensaje':'FORMULARIO INVALIDO'})
    else:
        formulario=AvatarForm()
        return render(request, "chat/user_AddAvatar.html", {"formulario":formulario, "usuario":request.user, "avatar": obteneravatar(request)})

def obteneravatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="media/avatares/avatarpordefecto.png"
    return imagen

@login_required
def user_Edit(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name  =info["first_name"]
            usuario.last_name   =info["last_name"]
            usuario.email       =info["email"]
            usuario.save()
            return render(request, "chat/inicio.html", {"mensaje":"Perfil Editado Exitosamente",'avatar':obteneravatar(request)})
        else:
            return render(request, "chat/user_Edit.html", {"formulario":form, "usuario":usuario, "mensaje":"FORMULARIO INVALIDO",'avatar':obteneravatar(request) })
    else:
        form= UserEditForm(instance=usuario)
        return render(request, "chat/user_Edit.html", {"formulario":form, "usuario":usuario,'avatar':obteneravatar(request)})

@login_required
def user_EditPass(request):
    usuario=request.user
    if request.method=="POST":
        form=UserPassEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.password1   =info["password1"]
            usuario.password2   =info["password2"]
            usuario.save()
            return render(request, "chat/inicio.html", {"mensaje":"Contraseña Actualizada",'avatar':obteneravatar(request)})
        else:
            return render(request, "chat/user_EditPass.html", {"formulario":form, "usuario":usuario, "mensaje":"FORMULARIO INVALIDO",'avatar':obteneravatar(request)})
    else:
        form= UserPassEditForm(instance=usuario)
        return render(request, "chat/user_EditPass.html", {"formulario":form, "usuario":usuario,'avatar':obteneravatar(request)})

@login_required
def user(request):
    return render(request, "chat/user.html",{'avatar':obteneravatar(request)}) 

@login_required
def user_MenuBlogs(request):
    return render(request, "chat/user_MenuBlogs.html",{'avatar':obteneravatar(request)}) 

@login_required
def form_blog(request):
    if request.method=="POST":
        formulario=BlogForm(request.POST, request.FILES)
        if formulario.is_valid():
            info        =formulario.cleaned_data
            objeto=Blog(
            usuario     =request.user,  
            titulo      =info["titulo"],
            subtitulo   =info["subtitulo"],
            cuerpo      =info["cuerpo"],
            autor       =info['autor'],
            fecha       =info["fecha"],
            imagen      =info["imagen"],
            )
            objeto.save()
            return render(request, "chat/form_blog.html", {'usuario':request.user, 'mensaje':'Formulario Creado Exitosamente', "imagen": objeto.imagen.url,'avatar':obteneravatar(request)})
        else:
            return render(request, "chat/form_blog.html", {"mensaje":"Error",'avatar':obteneravatar(request)})
    else:
        formulario=BlogForm()
        return render (request, "chat/form_blog.html", {"formulario":formulario ,'avatar':obteneravatar(request)})

@login_required
def blog_edit(request,id):
    blog=Blog.objects.get(id=id)
    if request.method=='POST':
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            info             =form.cleaned_data
            blog.titulo      =info["titulo"]
            blog.subtitulo   =info["subtitulo"]
            blog.cuerpo      =info["cuerpo"]
            blog.autor       =info['autor']
            blog.fecha       =info["fecha"]
            blog.imagen      =info["imagen"]
            blog.save()
            Blogs=Blog.objects.all()
            return render(request, 'chat/blog_edit.html',{'blog':blog,"imagen": blog.imagen.url,'Blogs':Blogs,'mensaje':"Blog Editado Exitosamente"})
        else:
            Blogs=Blog.objects.all()
            return render(request, 'chat/blog_edit.html',{'blog':blog,"imagen": blog.imagen.url,'Blogs':Blogs,'mensaje':"Faltan Campos por rellenar o Formulario Invalido"})
    else:
        form=BlogForm(initial={'titulo':blog.titulo,'subtitulo':blog.subtitulo,'cuerpo':blog.cuerpo,'autor':blog.autor,'fecha':blog.fecha,'imagen':blog.imagen.url})
        return render(request, 'chat/blog_edit.html',{'formulario':form, 'blog':blog})







@login_required
def user_MisBlogs(request):
    Blogs=Blog.objects.filter(usuario=request.user)
    return render(request, 'chat/user_MisBlogs.html',{'Blog':Blogs ,'avatar':obteneravatar(request)})


#Aplicacion de Chat
@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, 'chat/chat.html',
            {'users': User.objects.exclude(username=request.user.username)})

def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, "chat/messages.html",
            {'users': User.objects.exclude(username=request.user.username),
            'receiver': User.objects.get(id=receiver),
            'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
            Message.objects.filter(sender_id=receiver, receiver_id=sender)})


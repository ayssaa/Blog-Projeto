from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.models import User
from blog import models
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home/')
    return render(request, 'blog/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/login')
    return render(request, 'blog/signup.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    
    return render(request, 'blog/newpost.html')



def myPost(request):
    context = {
        'posts': Post.objects.filter(author= request.user)
    }
    return render(request, 'blog/mypost.html', context)



def signout(request):
    logout(request)
    return redirect('/login')


def post_details(request, pk):
    post = Post.objects.get(pk=pk)  # Aqui buscamos o post com o 'pk' fornecido na URL
    return render(request, 'blog/post_details.html', {'post':post})

def newcomment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment(post=post, content=content, author=request.user)
        comment.save()
        return redirect('/home')
    
    return render(request, 'blog/newcomment.html')
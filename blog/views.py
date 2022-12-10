from urllib import request
from django.shortcuts import render
from blog.models import Post


def home(request):        
    return render(request, 'blog/home.html')


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post 
    }
    return render(request, 'blog/post_detail.html', context)



def home2(request):       
    return render(request, 'blog/exemplos/home2.html')



def home3(request):
   return render(request, 'blog/exemplos/home3.html' )


def home4(request):
   return render(request, 'blog/exemplos/home4.html' )

def home5(request):
    return render(request, 'blog/exemplos/home5.html')


def home6(request):
    return render(request, 'blog/exemplos/home6.html')


def home7(request):
    return render(request, 'blog/exemplos/home7.html')


def colapse(request):
    return render(request, "blog/exemplos/colapse.html")
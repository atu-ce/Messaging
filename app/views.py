from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.



User = get_user_model()


from app.models import Post

def home(request):
    return render(request,"home.html")

@login_required(login_url="/login/") 
def anasayfa(request):
    makaleler = Post.objects.all()
    
    context = {
        "makaleler": makaleler
    }
    return render(request,"anasayfa.html",context)

@login_required(login_url="/login/") 
def profile(request):
    users=User.objects.all().exclude(id=request.user.id)
    posts=Post.objects.filter(author=request.user)

    if request.method == "POST":
        icerik = request.POST.get("icerik")
        baslik = request.POST.get("baslik")

        Post.objects.create(content=icerik,
                            title=baslik,
                            author=request.user)
        return redirect('/profile/')
    context = {
        "posts": posts,
        "users": users
    }
    return render(request,"profile.html",context)

def article_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        "makale": post
    }
    return render(request, "article.html", context)    

def about(request):
    return render(request,"about.html")
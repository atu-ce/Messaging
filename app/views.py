from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.
#internal
from app.models import Post, Comment, Message


User = get_user_model()




#Giriş yapılmadığındaki anasayfa:
def home(request):
    return render(request,"home.html")

#Giriş yapıldığındaki anasayfa:

@login_required(login_url="/login/") 
def anasayfa(request):
    users=User.objects.all().exclude(id=request.user.id)
    makaleler = Post.objects.all()
    
    context = {
        "makaleler": makaleler,
        "users": users
    }

    #Messaging Bölümü:

    if request.method == "POST":
        targetuser_id = request.POST.get("targetuser")
        mymessage = request.POST.get("mymessage")
        targetuser = User.objects.get(id=targetuser_id)
        Message.objects.create(
            body=mymessage,
            sender=request.user,
            receiver=targetuser
        )
        return redirect("/home/")
    

    return render(request,"anasayfa.html",context)

@login_required(login_url="/login/") 
def profile(request):
    users=User.objects.all().exclude(id=request.user.id)
    posts=Post.objects.filter(author=request.user)

    #Post yayınlama Bölümü:

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

    #Yorum Bölümü:

    if request.method == "POST":
        gelen_yorum = request.POST.get("yorum")

        Comment.objects.create(
            text=gelen_yorum,
            author=request.user,
            post=post
        )
        url = "/profile/"+str(post.id)
        return redirect(url)
    return render(request, "article.html", context)    

def about(request):
    return render(request,"about.html")
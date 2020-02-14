from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as lg, logout as lo , authenticate
from blogapp.models import Articles, getintouch
from django.contrib import messages




def home(request):
    return render(request, 'index.html')
    


def contact(request):
    if request.method == 'POST':
        username = request.POST['name']
        emailget = request.POST['emailget']
        issue = request.POST['message']
        touch = getintouch(username = username, email1=emailget , issue
        =issue)
        touch.save()


        

    return render(request, 'contact.html')

    
def article(request):
    arti = Articles.objects.all()
    params = {'arti':arti}
    return render(request, 'article.html', params)


def signup(request):
    if request.method == 'POST':
        username = request.POST['user']
        email = request.POST['mail']
        password1 = request.POST['password']
        password2 = request.POST['repassword']
        
        if len(username) > 30:
            messages.success(request, "username too long")
            return redirect ('home')

        if len(username) < 2:
            messages.success(request, "username too short")
            return redirect ('home')
        
        if password1 != password2:
            messages.success(request, "passwords donot match")
            return redirect ('home') 

        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        messages.success(request, 'you have successfully signup your account')
        return redirect ('home')
    
    else:
        return HttpResponse('404-not found')


def blogpost(request , pk):
    arti =Articles.objects.filter(pk=pk).values()
    params = {'arti':arti}
    return render(request, 'blogpost.html', params)


def login(request):
    if request.method == 'POST':
        signmail = request.POST['signmail']
        signpawd = request.POST['signpawd']
        user = authenticate(username = signmail , password= signpawd )
        if user is not None:
            lg(request , user)
            messages.success(request, 'you have successfully login into your account')
            return redirect ('home')
        else:
            messages.error(request, 'already creates')
            return redirect ('home')
    return HttpResponse("error ")

def logout(request):
    lo(request)
    messages.success(request, 'sucessifully logout')
    return redirect ('home')

def search(request):
    query = request.GET['query']
    if len(query)>50:
        arti = []
        return HttpResponse('search correctily')
    else:
        arti = Articles.objects.filter(title__icontains=query)
    if arti.count() == 0:
      
         return HttpResponse('<h1>Nothing To search</h1>')
    else:
        params = {'arti':arti}
    return render(request, 'search.html', params)

def addarticles(request):
    if request.method=='POST':
        user = request.POST['user']
        title = request.POST['title']
        desc = request.POST['desc']
        date = request.POST['date']
        url = request.POST['url']
        blog = Articles(username= user, title = title ,description=desc, date = date,
        image = url)
        blog.save()
    return render(request, 'addarticle.html')
  


      

        


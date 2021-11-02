from django.shortcuts import render
from django.contrib.auth.models import auth
from django.shortcuts import redirect
from django.contrib import messages
from .forms import PostForm
from .models import Post


# Create your views here.
def test(request):
    return render(request, 'test2.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')


def postforms(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('/')
    else:
        print(request.user)
        form = PostForm()
        context = {
            "form": form,
        }
        return render(request, 'test.html', context)


def postforms2(request):
    if request.method == 'POST':
        text = request.POST.get('Text')
        Post.objects.create(user=request.user,text=text)
        return redirect('/')
    else:
        print(request.user)
        return render(request,'test2.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

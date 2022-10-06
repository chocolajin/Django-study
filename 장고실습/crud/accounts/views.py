from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_http_methods(['GET','POST'])
def login(request):
    # 로그인된 사용자는 로그인 못하게
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method=='POST':
        # 첫 인자는 request
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
        # 장고가 제공하는 로그인 기능 사용해서 로그인하기
            auth_login(request, form.get_user())       
            return redirect(request.GET.get('next') or'articles:index')
        
    else: # 장고가 제공하는 로그인 폼 사용
        form =AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')
        
@require_http_methods(['GET','POST'])
def signup(request):
    # 로그인된 사용자면 회원가입 못함
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 회원가입도 전용 폼 있음
    # 바로 사용못함 사용 클래스가 다른 클래스다
    # usercreationform 재정의 accounts/form.py에
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST,instance =request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')    
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    pass
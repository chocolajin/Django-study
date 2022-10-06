from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, CommentForm
# Create your views here.
@require_safe
def index(request):
    #db에서 게시글 목록 가져온 다음 템플릿에 보내주기
    # 모델 클래스의 오브젝츠 매니저를 통해 데이터 조회
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
@require_safe
def detail(request,pk):
    # pk를 이용해서 db 조회, context에 담아 전달
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()   
    context = {
        'article' : article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request,'articles/detail.html',context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:    
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail',article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form' : form,
        'article': article,
    }
    return render(request,'articles/update.html',context)

# @login_required 하면안돼 
@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
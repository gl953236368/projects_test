from django.shortcuts import render,get_object_or_404,redirect,Http404
from .models import Article,Tag,Comments
from django.contrib import auth

def login(request,article_id):
    username = request.POST.get('userName', '')
    password = request.POST.get('pasWord', '')
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('myblogs:detail', article_id)
    else:
        raise Http404('Error,the page was losed.')



# 注销
def loginout(request,article_id):

    auth.logout(request)

    return redirect('myblogs:detail', article_id)




# Create your views here.
def get_home(request):
    article = Article.objects.order_by('pub_date')[:5]
    context = {
        'articles': article
    }
    return render(request, 'blogs/home.html', context)


def get_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comments.objects.filter(article=article_id)
    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'blogs/details.html', context)


def save_comments(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    content = request.POST.get('content')
    user = auth.get_user(request)
    comment = Comments(article=article, visterName=user.username, content=content)
    comment.save()
    #Comments.object.create(comment)
    return redirect('myblogs:detail', article_id)

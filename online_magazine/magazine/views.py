from django.shortcuts import render
from .models import Article


# Create your views here.

def article_view(request, pk=None):
    if pk:
        template_ = 'full_title.html'
        current_article = Article.objects.get(pk=pk)
        context = {
            'current_article': current_article
        }
        return render(request, template_name=template_, context=context)
    else:
        template_ = 'titles.html'
        articles = Article.objects.all()
        context = {
            'arts': articles
        }
        return render(request, template_name=template_, context=context)


def change_article(request) -> render:
    template_ = 'titles.html'
    articles = Article.objects.all()

    context = {
        'arts': articles
    }
    for i in articles:
        if str(i.pk) not in i.title:
            i.title = f'{i.title} - {i.pk}'
            i.save()

    return render(request, template_name=template_, context=context)

def delete_article(request) -> render:
    template_ = 'titles.html'
    articles = Article.objects.all()

    context = {
        'arts': articles
    }
    for i in articles:
        if i.pk % 2 == 1:
            i.delete()

    return render(request, template_name=template_, context=context)
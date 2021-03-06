from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import News, Category


def index(request):
    news = News.objects.all()
    # categories = Category.objects.all() -> news_tags.py -> get_categoris
    context = {
        'news': news,
        'title': 'News list',
        # 'categories': categories
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    # categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
        # 'categories': categories
    }
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'item': news_item,
    }
    return render(request, 'news/view_news.html', context)

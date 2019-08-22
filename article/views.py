from django.shortcuts import render, render_to_response  # convert variable
from django.http import HttpResponse, Http404
from .models import Article

# Create your views here.
def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        context = {}
        context['article_obj'] = article
        return render_to_response("article_detail.html", context)
        #return render(request, "article_detail.html", context)
    except Article.DoesNotExist:
        raise Http404('not exist')

def article_list(request):
    #articles = Article.objects.all()
    articles = Article.objects.filter(is_delete=False)
    context = {}
    context['articles'] = articles
    return render_to_response("article_list.html", context)

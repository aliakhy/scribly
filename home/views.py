from django.shortcuts import render
from article.models import Article


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from .form import Articlecreate,Articleedite
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from categories.models import Category


def article_page(request):
     articles = Article.objects.filter(is_show=True)
     categories = Category.objects.all()
     search_keyword = request.GET.get('search')
     category_id = request.GET.get('category')
     if category_id:
          articles = articles.filter(categories=category_id)
     if search_keyword:
          articles = articles.filter(title__icontains=search_keyword).distinct()
     paginator = Paginator(articles.order_by('-update_date'),6)
     page_number = request.GET.get('page')
     page_object= paginator.get_page(page_number)

     context={'page_object': page_object,
              'categories': categories,
              }

     return render(request,'article/article_list.html',context)


def article_detail(request,article_id):
     article=get_object_or_404(Article,id=article_id)
     categories=article.categories.all()
     context={'articles': article,
              'categories': categories}

     return render(request, 'article/article_detail.html', context)



@login_required()
def article_create(request):
     form = Articlecreate(data=request.POST or None, files=request.FILES or None )
     if form.is_valid():

          artticle_title = form.cleaned_data.get('title')
          artticle_text = form.cleaned_data.get('text')
          artticle_picture = form.cleaned_data.get('picture')
          artticle_is_show = form.cleaned_data.get('is_show')
          article_category = form.cleaned_data.get('categories')

          article=Article.objects.create(
               title=artticle_title,
               text=artticle_text,
               picture=artticle_picture,
               is_show=artticle_is_show,
               author=request.user,
          )

          article.categories.set(article_category)
          return  redirect('article:article_list')

     context={'form':form}
     return render(request,'article/creat_article.html',context)


@login_required()
def article_edite(request, article_id):
     article=get_object_or_404(Article, id=article_id)
     if request.method=='GET':
          form=Articleedite(initial={'title':article.title,'text':article.text,'is_show':article.is_show,'categories':article.categories.all()})
     else:
          form = Articleedite(data=request.POST, files=request.FILES)
          if form.is_valid():
               artticle_title = form.cleaned_data.get('title')
               artticle_text = form.cleaned_data.get('text')
               artticle_picture = form.cleaned_data.get('picture')
               artticle_is_show = form.cleaned_data.get('is_show')
               article_category = form.cleaned_data.get('categories')
               article.title = artticle_title
               article.text = artticle_text
               if artticle_picture:
                    article.picture = artticle_picture
               article.is_show = artticle_is_show
               article.categories.set(article_category)
               article.save()
               return redirect('article:article_detail',article_id=article.id)


     context={'article': article,'form': form}
     return render(request,'article/article_edite.html',context)

@login_required
def article_delete(request,article_id):

     article=get_object_or_404(Article,id=article_id,author_id=request.user.id)
     article.delete()
     return redirect('article:article_list')



def category(request, category_id):
     articles=Article.objects.filter(categories=category_id,is_show=True)

     search_keyword = request.GET.get('search')
     if search_keyword:
          articles = articles.filter(title__icontains=search_keyword).distinct()
     paginator = Paginator(articles.order_by('id'), 6)
     page_number = request.GET.get('page')
     page_object = paginator.get_page(page_number)

     context={'page_object':page_object}
     return render(request,'article/article_list.html', context)

def error(request):
     return render(request, 'templates/user/register/error.html')



from django.urls import path
from .views import *
app_name='article'



urlpatterns =[
    path('',article_page,name='article_list'),
    path('detail/<int:article_id>/',article_detail,name='article_detail'),
    path('create/',article_create,name='article_create'),
    path('edite/<int:article_id>/',article_edite,name='article_edite'),
    path('delete/<int:article_id>/',article_delete,name='article_delete'),
    path('category/<int:category_id>/',category,name='article_category'),

    path('error/',error,name='error'),

]

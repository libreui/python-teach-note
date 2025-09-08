from django.http import HttpResponse
from django.shortcuts import render
from ..models import Post
# Create your views here.


def index(request):
    # 视图中获取模型数据
    posts = Post.objects.all()
    # 渲染模板并传递数据
    return render(request, 'home/index.html', {'posts': posts})
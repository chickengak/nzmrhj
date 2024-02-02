from django.shortcuts import render, redirect           # response의 응답페이지 함수
from django.http import HttpResponse, JsonResponse      # 응답페이지의 형식

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html")
# Create your views here.

def my_render_view(request):
    ## 계산용 비즈니스 로직을 추가한다.
    context = {"a":1, "b":2}
    return render(request, "my_template.html", context) # 템플릿으로 렌더링


def left_sidebar_view(request):
    return render(request, "left-sidebar.html")

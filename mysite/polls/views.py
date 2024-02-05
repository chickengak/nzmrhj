from django.shortcuts import render, redirect           # response의 응답페이지 함수
from django.http import HttpResponse, JsonResponse      # 응답페이지의 형식
from .models import InputDataModel
from django.contrib import messages
from .utils import *

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html")

def left_sidebar_view(request):
    return render(request, "left-sidebar.html")

def right_sidebar_view(request):
    return render(request, "right-sidebar.html")

def no_sidebar_view(request):
    return render(request, "no-sidebar.html")


def createform(request):

    if request.method == 'POST':
        data = InputDataModel()

        data.area = request.POST['area']  # <class 'polls.models.InputDataModel'> <class 'str'>
        data.trans_floor = request.POST['trans_floor']
        data.com_year = request.POST['com_year']
        data.interest = request.POST['interest']
        data.household = request.POST['household']
        data.top_floor = request.POST['top_floor']
        data.subway_dist = request.POST['subway_dist']
        data.subway_cnt = request.POST['subway_cnt']
        data.bus_cnt = request.POST['bus_cnt']
        data.parking_lot = request.POST['parking_lot']
        data.school = request.POST['school']
        data.hospital = request.POST['hospital']
        res = 'myres' #predict_value([data.area, data.trans_floor])
        res = model_pkl_predict([84.046, 16.0, 2019.0, 3.5, 4932.0, 35.0, 0.3049339773051127, 1.0986122886681098, 3.9512437185814275, 1.45316301703163, 11.0, 0.0])
        messages.success(request, f'예측 전세가 　 {res} 만원')

    return redirect('index')
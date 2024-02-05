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
        data.apt_age = request.POST['apt_age']
        data.interest = request.POST['interest']
        data.top_floor = request.POST['top_floor']
        data.bus_cnt = request.POST['bus_cnt']
        data.parking_lot = request.POST['parking_lot']
        data.school = request.POST['school']
        data.household = request.POST['household']

        data.gangnam_3gu = request.POST['gangnam_3gu']
        data.ent_type_stair = request.POST['ent_type_stair']
        data.ent_type_corridor = request.POST['ent_type_corridor']

        user_inputs = [data.area, data.trans_floor, data.apt_age, data.interest, data.top_floor, data.bus_cnt, data.parking_lot,
                         data.school, data.household, data.gangnam_3gu, data.ent_type_stair, data.ent_type_corridor]
        user_inputs_float = []
        for ui in user_inputs:
            try:
                user_inputs_float.append(float(ui))
            except ValueError:
                messages.success(request, f'올바른 입력을 해주세요!')
                return redirect('index')
        user_inputs[5] = np.log(user_inputs[5]+1)
        res = model_pkl_predict(user_inputs_float)
        # user_inputs = [84.53, 4.0, 15.0, 3.25, 13.0, 4.574710978503383, 1.1073094867807154, 22.0, 643.0, 0.0, 1.0, 0.0]
        # res = model_pkl_predict(user_inputs)
        messages.success(request, f'예측 전세가 　 {res} 만원')

    return redirect('index')
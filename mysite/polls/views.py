from django.shortcuts import render, redirect           # response의 응답페이지 함수
from django.http import HttpResponse, JsonResponse      # 응답페이지의 형식
from .models import InputDataModel

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

        data.area = request.POST['area']
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

        data.save()

    return redirect('index')
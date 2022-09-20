from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    '''
    视图函数，至少一个参数
    :param request: 接收请求对象
    :return: 响应对象
    '''
    return HttpResponse('hello,world!')
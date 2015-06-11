#coding:UTF-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
import graphviz_web.settings
import manage
def index(request):
    return HttpResponse(u'Hello World')

def get_video_result(request):
    key1 = request.GET.get('lquery')
    key2 = request.GET.get('rquery')
    print key1, key2
    res_list = graphviz_web.settings.graph.get_query_connection(key1,key2)
    content = 'Insight<br/>'
    for res in res_list:
        content += res[0].encode('utf-8')+'<br/>'
    return HttpResponse(content)
# Create your views here.

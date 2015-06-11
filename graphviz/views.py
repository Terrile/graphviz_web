#coding:UTF-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
import graphviz_web.settings
from django.template.loader import get_template
import manage
def index(request):
    return HttpResponse(u'Hello World')

def get_video_result(request):
    key1 = request.GET.get('lquery')
    key2 = request.GET.get('rquery')
    print key1, key2
    query_list = graphviz_web.settings.graph.get_query_connection(key1,key2)
    content = 'Insight<br/>'
    query_res_list = []
    for res in query_list:
        #content += res[0].encode('utf-8')+'<br/>'
        query_res_list.append(res[0].encode('utf-8'))
    video_list = graphviz_web.settings.graph.get_video_connection(key1,key2)
    video_res_list = []
    for res in video_list:
        video_res_list.append(res[0].encode('utf-8'))
    template = get_template('insight.html')
    html = template.render(Context({'videolist':video_res_list,'querylist':query_res_list}))
    return HttpResponse(html)
#    return HttpResponse(content)

# Create your views here.

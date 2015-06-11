from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'^$', 'graphviz.views.index', name='home'),
    url(r'^$', 'graphviz.views.index', name='home'),
    #url(r'^compare.*q1.*q2.*$', 'graphviz.views.get_video_result', name='Connection'),
    url(r'^insight', 'graphviz.views.get_video_result', name='Connection'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

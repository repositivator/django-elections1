from django.conf.urls import include, url
from . import views            # . : 현재폴더를 의미 & views 모델을 import

app_name = "elections"
urlpatterns = [
    url(r'^$', views.index, name = 'home'), # $ : 빈 경로를 의미
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results/$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^candidates/(?P<name>[가-힣]+)/$', views.candidates)
]

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^(?P<post>[-\w]+)/$',views.post_detail,name='post_detail')
]

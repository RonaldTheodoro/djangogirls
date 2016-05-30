from django.conf.urls import url
from mysite.blog.views import post_list, post_detail, post_new, post_edit


urlpatterns = [
    url(r'^$', post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
]

from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prefetch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^granpa1/', views.index1),
    url(r'^granpa2/', views.index2),
)

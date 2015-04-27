from django.contrib import admin
from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prefetch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('app1.urls')),
)

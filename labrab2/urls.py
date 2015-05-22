from django.conf.urls import include,patterns, url
from django.contrib import admin
from labrab2.views import IndexView
'''
urlpatterns = [
    # Examples:
    # url(r'^$', 'labrab2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
'''
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view()),
)
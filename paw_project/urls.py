from django.conf.urls import patterns, include, url
from django.contrib import admin
from paw_project import settings
from . import views
import poems

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'paw_project.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^', )),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^writers/', include('poems.urls'), ),
                       url(r'^related_links/$', views.related_links, name="related links"),
                       url(r'^contact/$', views.contact, name="contact"),
                       url(r'^videos/$', views.videos, name="videos"),
                       url(r'^$', views.home, name="home"),
                       url('^markdown/', include('django_markdown.urls')),
                       )

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))
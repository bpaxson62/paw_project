__author__ = 'brian'
from django.conf.urls import patterns, include, url
from poems import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paw_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^', )),
    url(r'^$', views.WriterIndex.as_view(), name='writer_index'),
    url(r'^bio/(?P<writer_slug>\S+)/$', views.writer_detail, name="writer_detail"),
    url(r'^poems/(?P<writer_slug>\S+)$', views.writer_poems, name="writer_poems"),
    url(r'^publications/(?P<writer_slug>\S+)$', views.writer_publications, name="writer_publications"),
    # url(r'^writer', include(poems.urls)),
)

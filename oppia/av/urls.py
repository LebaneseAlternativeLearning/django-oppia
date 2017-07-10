# oppia/av/urls.py
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
   url(r'^$', 'oppia.av.views.home_view', name="oppia_av_home"),
   url(r'^upload/$', 'oppia.av.views.upload_view', name="oppia_av_upload"),
   url(r'^upload/success/(?P<id>\d+)$', 'oppia.av.views.upload_success_view', name="oppia_av_upload_success"),
)

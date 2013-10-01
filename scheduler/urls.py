__author__ = 'thomas'
from django.conf.urls import patterns, include, url
from .views import IndexView, Ledger, AppointmentDate, AppointmentDay, AppointmentDetail


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^ledger/$', Ledger.as_view(), name='ledger'),
    url(r'^(?P<pk>\d)$', AppointmentDetail.as_view(), name='detail'),
    url(r'^(?P<year>\d{4})/week/(?P<week>\d+)/$', AppointmentDate.as_view(), name='week_view'),
    url(r'^(?P<year>\d{4})/(?P<month>[-\w]+)/(?P<day>\d+)/$', AppointmentDay.as_view(), name='day_view'),
)
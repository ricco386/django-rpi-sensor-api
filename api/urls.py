from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^units/$', views.UnitList.as_view()),
    url(r'^units/(?P<name>[a-zA-Z0-9]+)/$', views.UnitDetail.as_view()),
    url(r'^sensors/$', views.SensorList.as_view()),
    url(r'^sensors/(?P<name>[a-zA-Z0-9]+)/$', views.SensorDetail.as_view()),
    url(r'^nodes/$', views.NodeList.as_view()),
    url(r'^nodes/(?P<name>[a-zA-Z0-9]+)/$', views.NodeDetail.as_view()),
    url(r'^measurements/$', views.MeasurementList.as_view()),
    url(r'^measurements/(?P<pk>[0-9]+)/$', views.MeasurementDetail.as_view()),
]

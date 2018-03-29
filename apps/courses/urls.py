from django.conf.urls import include, url
from . import api
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^courses/all/$', views.CourseView.as_view(),
        name="all_course"),
    url(r'^enroll/$', api.EnrollCourseView.as_view(),
        name="enroll"),
    url(r'^quit/$', api.QuitCourseView.as_view(),
        name="quit"),
]

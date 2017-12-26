"""BlackBoard_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# Serializers define the API representation.
from rest_framework import routers
# Routers provide an easy way of automatically determining the URL conf.
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from app import views
from choices_data import views as ChoicesViews

schema_view = get_schema_view(title='BlackBoard API')
router = routers.DefaultRouter()
router.register(r'faculties', views.FacultyViewSet)
router.register(r'classes', views.ClassViewSet)
router.register(r'schedules', views.ScheduleViewSet)
router.register(r'responsibilities', views.ResponsibilityViewSet)
router.register(r'dept-choices', ChoicesViews.DeptChoicesViewSet)
router.register(r'faculty-choices', ChoicesViews.FacultyChoicesViewSet)
router.register(r'room-choices', ChoicesViews.RoomChoicesViewSet)
router.register(r'block-choices', ChoicesViews.BlockChoicesViewSet)
router.register(r'subject-choices', ChoicesViews.SubjectChoicesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth', views.AuthViewSet.as_view()),
    url(r'^availability', views.AvailabiltyViewSet.as_view()),
    url(r'^docs/', include_docs_urls(title='BlackBoard API Documentation'))
]

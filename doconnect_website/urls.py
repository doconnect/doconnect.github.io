"""doconnnect_server URL Configuration

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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^patient/$', views.patient ,name='patient'),
    url(r'^doctor/$', views.doctor, name='doctor'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^patient_login/$', views.patient_login, name='patient_login'),
    url(r'^validate_username/$', views.validate_username, name='validate_username')
]
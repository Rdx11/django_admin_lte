from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from rest_framework_jwt.views import (obtain_jwt_token,
                                        verify_jwt_token,
                                        refresh_jwt_token)
from admin_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^token_auth', obtain_jwt_token),
    url(r'^token_refresh', refresh_jwt_token),
    url(r'^token_verify', verify_jwt_token),
    url(r'^register', views.CreateUser.as_view()),
    url(r'^login', views.LoginUser.as_view()),
    url(r'^dashboard', views.DashboardDetail.as_view())
]

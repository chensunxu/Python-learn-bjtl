from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 视图函数名称只有名称，无括号和参数
    url(r'^chensunxu/', views.do_app),
]


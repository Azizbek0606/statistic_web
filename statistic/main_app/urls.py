from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.home, name="home"),
    path("statistic/", views.statistic, name="statistic"),
    path("api/daily/work", views.Daily_work_send_api.as_view(), name="post_list"),
]

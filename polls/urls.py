from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.select_table, name='work_page')
    ]
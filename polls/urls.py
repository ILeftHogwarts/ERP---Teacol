from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.WorkPageView.as_view(), name='work page')]
from django.conf.urls import url
from django.contrib import admin

from cache import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index',),
    url(r'^inc/', views.inc, name='inc',),
    url(r'^income/', views.IncomeView, name='income',),
    url(r'^name/', views.name, name='name',),

]

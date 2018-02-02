from django.contrib import admin
from django.conf.urls import url
from companies import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^stocks/', views.StockList.as_view()),
    url(r'^admin/', admin.site.urls),
]

urlpatterns=format_suffix_patterns(urlpatterns)

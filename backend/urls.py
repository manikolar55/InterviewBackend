from django.urls import path
# from .views import Backend
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import ChartData

urlpatterns = [
    path("chart/data", ChartData.as_view(), name="charts"),

]


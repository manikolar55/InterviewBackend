from django.urls import path
from .views import ChartData, FetchData

urlpatterns = [
    path("chart/data", ChartData.as_view(), name="charts"),
    path("fetch/data", FetchData.as_view(), name="fetch_data")

]


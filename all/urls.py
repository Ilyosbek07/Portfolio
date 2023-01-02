from django.urls import path

from all.views import PortfolioView

app_name = 'all'

urlpatterns = [
    path('', PortfolioView.as_view(), name='main')
]
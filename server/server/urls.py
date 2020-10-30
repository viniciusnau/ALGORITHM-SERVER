from django.contrib import admin
from django.urls import path

from algorithms.views import algorithm_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>/', algorithm_view),
    path('-<int:pk>/', algorithm_view),
]

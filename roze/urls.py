from django.urls import path
from .views import RozeListView, RozeDetailView

urlpatterns = [

    path('', RozeListView.as_view(), name= 'Roze_list'),
    path('<int:pk>/',RozeDetailView.as_view(), name= 'Roze_detail')
]
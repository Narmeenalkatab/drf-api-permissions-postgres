from django.urls import path
from .views import RozeListView, RozeDetailView, PostListView,PostDetailView

urlpatterns = [
    path('', RozeListView.as_view(), name= 'Roze_list'),
    path('<int:pk>/',RozeDetailView.as_view(), name= 'Roze_detail'),
    path('post/', PostListView.as_view(), name= 'post_list'),
    path('post/<int:pk>/',PostDetailView.as_view(), name= 'post_detail')

]

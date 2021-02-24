from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('blessings/', views.BlessingList.as_view(), name='blessing_list'),
    path('blessings/<int:pk>', views.BlessingDetail.as_view(), name='blessing_detail'),
    path('comment/', views.CommentList.as_view(), name='comment_list'),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment_detail')
]
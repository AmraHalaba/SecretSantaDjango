from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.MemberList.as_view(), name="members"),

    path('<str:pk>/', views.MemberDetail.as_view(), name="member"),
    path('<str:pk>/delete/', views.MemberDelete.as_view(), name="delete"),
]
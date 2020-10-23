from django.urls import path
from . import views 

urlpatterns = [
    path('message', views.MessageListView.as_view()),
    path('message/<pk>',views.MessageDetailView.as_view()),
    path('chat',views.ChatListView.as_view()),
    path('chat/<pk>',views.ChatDetailView.as_view())
]
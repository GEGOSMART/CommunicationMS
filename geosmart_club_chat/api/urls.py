from geosmart_club_chat.api.views import (
    MessageViewSet, 
    ChatListView,
    ChatDetailView,
    ChatCreateView,
    ChatUpdateView,
    ChatDeleteView,
    ContactViewSet)
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contact',ContactViewSet, basename='contact')
router.register(r'message',MessageViewSet, basename='message')
#router.register(r'chat',ChatViewSet, basename='chat')

urlpatterns = [
    path('chat', ChatListView.as_view()),
    path('chat/<pk>', ChatDetailView.as_view()),
    path('chat/create/',ChatCreateView.as_view()),
    path('chat/update/<pk>',ChatUpdateView.as_view()),
    path('chat/delete/<pk>',ChatDeleteView.as_view()),
]

urlpatterns += router.urls

# from django.urls import path
# from .views import (
#     MessageListView,
#     MessageDetailView,
#     MessageCreateView,
#     MessageUpdateView,
#     MessageDeleteView,
#     ChatListView,
#     ChatDetailView,
#     ChatCreateView,
#     ChatUpdateView,
#     ChatDeleteView
# )

# urlpatterns = [
#     path('message', MessageListView.as_view()),
#     path('message/<pk>', MessageDetailView.as_view()),
#     path('message/create/', MessageCreateView.as_view()),
#     path('message/update/<pk>',MessageUpdateView.as_view()),
#     path('message/delete/<pk>',MessageDeleteView.as_view()),
#     path('chat', ChatListView.as_view()),
#     path('chat/<pk>', ChatDetailView.as_view()),
#     path('chat/create/',ChatCreateView.as_view()),
#     path('chat/update/<pk>',ChatUpdateView.as_view()),
#     path('chat/delete/<pk>',ChatDeleteView.as_view()),
# ]


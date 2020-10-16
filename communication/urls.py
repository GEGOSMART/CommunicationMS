from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('geosmart_club_chat.urls', namespace='chat')),
]

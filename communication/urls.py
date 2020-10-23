from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('geosmart_club_chat.urls', namespace='chat')),
    path('api/', include('geosmart_club_chat.api.urls'))
]

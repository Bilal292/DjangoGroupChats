
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include ('myapp.urls')),
    path('chats/', include ('groupchat.urls')),
    path('admin/', admin.site.urls),
]

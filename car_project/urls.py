
from django.contrib import admin, include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.url')),
    path('accounts/', include('accounts.url')),
    path('showcars/', include('showcars.url')),
]

from django.contrib import admin
from django.urls import path, include

from .yasg import docsurlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api'))
]

urlpatterns += docsurlpatterns

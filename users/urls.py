from django.urls import path
from .views import CustomUserCreate
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name='create_user'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
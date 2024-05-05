from django.urls import path
from .views import CustomUserCreate
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name='create_user'),
]

urlpatterns += staticfiles_urlpatterns()
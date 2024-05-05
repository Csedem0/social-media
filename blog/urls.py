from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
]

urlpatterns += staticfiles_urlpatterns()
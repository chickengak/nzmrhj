from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("render/", views.my_render_view, name="my_render_view"),
    path("", views.index, name="index"),
    path("left-sidebar/", views.index, name="left_sidebar_view"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

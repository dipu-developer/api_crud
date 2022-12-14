from django.contrib import admin
from django.urls import path
from start import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/',views.fatch_api),
]

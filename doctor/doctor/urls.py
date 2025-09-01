from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctor_App.urls')),  # include your app, not the project
    path("accounts/", include("django.contrib.auth.urls")),  # 🔑 built-in auth

]




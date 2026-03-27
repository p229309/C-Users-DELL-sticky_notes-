from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# Ye main routing file hai
urlpatterns = [
    path('admin/', admin.site.urls),

    # App connect karna
    path('', include('notes.urls')),

    # Login / Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
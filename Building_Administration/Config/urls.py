from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView  



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Administration', include('Administration.urls')),
    path('Expenses', include('Expenses.urls')),
    path('', include('Admin.urls')),
    path('login/',LoginView.as_view(template_name ="Admin/login.html"),name ="login"),
    path('logout/',LogoutView.as_view(template_name ="login.html"), name="logout"),
]


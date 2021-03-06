from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView  



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Expenses', include('Expenses.urls')),
    path('mipanel/',include('Admin.urls')),
    path('accounts/login/',LoginView.as_view(template_name ="Admin/login.html"),name ="login"),
    path('logout/',LogoutView.as_view(template_name ="Admin/login.html"), name="logout"),
    path('', include('Main.urls')),
    path('homeowners/', include('Homeowners.urls')),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Administration', include('Administration.urls')),
    path('Expenses', include('Expenses.urls'))
]

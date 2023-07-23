from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
]
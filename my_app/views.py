from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

def hello_world(request):
    return HttpResponse("Hello, World!")
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  
]

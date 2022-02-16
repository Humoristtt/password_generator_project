from django.urls import path, include

urlpatterns = [
    path('', include('generator.urls'), name='home'),
    path('password/', include('generator.urls'), name='password'),
]

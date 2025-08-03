from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='http://localhost:3000/'), name='logout'),
    path('', admin.site.urls),
]
